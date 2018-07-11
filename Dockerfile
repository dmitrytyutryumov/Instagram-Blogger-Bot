FROM python:3.6

ARG PROJECT_DIR=/opt/instbot

RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev
RUN mkdir /db
RUN /usr/bin/sqlite3 /db/ibot.db

RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR

ADD . $PROJECT_DIR

RUN pip install --no-cache-dir -r requirements.txt

CMD ["celery", "worker", "-A", "etc.tasks", "-B", "--loglevel=info"]