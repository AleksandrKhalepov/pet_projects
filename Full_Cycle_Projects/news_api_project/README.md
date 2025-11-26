"Netflix perception in the media using sentiment analysis"

Project goal:
Development and implementation of a fully automated system for monitoring and evaluating the dynamics of the tonality of Netflix publications in the media at the present time.

Completed tasks and key results:

Designed and implemented data collection in Python using the Requests library for daily downloading of news articles via NewsAPI.

I conducted a Sentiment Analysis of the headlines using the TextBlob library to determine the polarity of each publication.

Deployed PostgreSQL to store the source data and analysis results.

Also, I used DBeaver to check performance at separate stages.

Configured Apache Airflow to automate the ETL pipeline, ensuring daily, reliable launch of all tasks

Developed an interactive BI dashboard in Apache Superset for visualizing key metrics.

Stack:
-Data source: NewsApi
-Infrastructure: Docker Compose, Gitlab, PyCharm
-Pipeline: Python, TextBlob, Pandas, Request
-Orchestrator: Apache Airflow
-Data storage and management: PostgreSQL, DBeaber
-BI and reporting: Apache Superset
