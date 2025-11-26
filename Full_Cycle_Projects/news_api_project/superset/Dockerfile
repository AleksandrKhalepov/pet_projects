FROM apache/superset:3.1.1

# Переключаемся на root, чтобы установить системные зависимости
USER root

# 1. Устанавливаем системные библиотеки, необходимые для КОМПИЛЯЦИИ psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    build-essential \
    && apt-get clean

# 2. Устанавливаем "дополнение" [postgres] для apache-superset
#    Это скажет pip установить psycopg2 (не бинарный) и все, что ему нужно.
#    Мы не устанавливаем psycopg2-binary!
RUN pip install --no-cache-dir "apache-superset[postgres]"

# 3. Возвращаемся к обычному пользователю
USER superset