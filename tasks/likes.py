from celery import Celery
from celery.schedules import crontab
from celery.task import periodic_task

from etc import Likes
from etc.constants import (
    TAGS_FOR_LIKE, USER, PASSWORD, MAX_LIKES, AMQP_URL, LIKES_SCHEDULE_HOURS,
    LIKES_SCHEDULE_MINS)

app = Celery(broker=AMQP_URL)


@periodic_task(
    run_every=(crontab(
        minute=LIKES_SCHEDULE_MINS, hour=LIKES_SCHEDULE_HOURS)
    ),
    name="run_bot", ignore_result=True)
def run_bot():
    Likes(USER, PASSWORD, TAGS_FOR_LIKE, MAX_LIKES).run_round_safe()
