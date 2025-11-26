from airflow.sdk import dag, task
from airflow.hooks.base import BaseHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from sqlalchemy import create_engine
from datetime import datetime
import requests
import pandas as pd
from textblob import TextBlob

@task
def fetch_data():
    connection = BaseHook.get_connection('news_api')
    api_key = connection.password
    params = {
    'q': 'netflix',
    'apiKey': api_key,
    'language': 'en'
    }
    base_url = 'https://newsapi.org/v2/everything'
    r = requests.get(base_url, params=params)
    r.raise_for_status()
    return r.json()

@task
def transform_data(json_data):
    articles = json_data['articles']
    df_raw = pd.DataFrame(articles)
    df = df_raw[['author', 'title', 'url', 'publishedAt']]
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    return df

def sentiment_func(text):
    blob = TextBlob(str(text))
    return blob.sentiment.polarity

@task
def apply_sentiment(df):
    df['sentiment'] = df['title'].apply(sentiment_func)
    return df

@task
def create_db_table():
    hook = PostgresHook(postgres_conn_id='postgres_news_db')
    sql="""
        CREATE TABLE IF NOT EXISTS news_table (
            title TEXT,
            author TEXT,
            url TEXT,
            publishedat TIMESTAMP WITH TIME ZONE,
            sentiment FLOAT,
            CONSTRAINT rule UNIQUE (url, publishedat)
        );
    """
    hook.run(sql)
@task
def upload_to_db(df):
    hook = PostgresHook(postgres_conn_id='postgres_news_db')
    engine = hook.get_sqlalchemy_engine()
    table_name = 'news_table'
    temp_table_name = 'temp_table'
    df.columns = [c.lower() for c in df.columns]
    df.to_sql(
        temp_table_name,
        con=engine,
        if_exists="replace",
        index=False,
    )
    columns = ", ".join(df.columns)
    sql_query = f"""
    INSERT INTO {table_name} ({columns})
    SELECT {columns}
    FROM {temp_table_name}
    ON CONFLICT (url, publishedat) DO NOTHING;
    """
    hook.run(sql_query)

@dag(
    dag_id='news_pipeline',
    start_date=datetime(2025, 1, 1),
    schedule='@hourly',
    catchup=False
)
def api_pipeline():
    raw_data = fetch_data()
    transformed_df = transform_data(raw_data)
    sentiment_df = apply_sentiment(transformed_df)
    table_created_task = create_db_table()
    upload_task = upload_to_db(sentiment_df)
    table_created_task >> upload_task

api_pipeline()