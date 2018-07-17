from celery import Celery
from celery.schedules import crontab
from celery.task import periodic_task
from selenium import webdriver

from etc import Dowloader, Uploder
from etc import Likes
from etc.constants import (
    DRIVER_PATH, UPLOAD_SCHEDULE_HOURS,
    UPLOAD_SCHEDULE_MINS
)
from etc.constants import (
    TAGS_FOR_LIKE, USER, PASSWORD, MAX_LIKES, AMQP_URL,
    DOWNLOAD_SCHEDULE_MINS, DOWNLOAD_SCHEDULE_HOURS, LIKES_SCHEDULE_MINS,
    LIKES_SCHEDULE_HOURS
)

app = Celery(broker=AMQP_URL)


@periodic_task(
    run_every=(crontab(
        minute=DOWNLOAD_SCHEDULE_MINS, hour=DOWNLOAD_SCHEDULE_HOURS)
    ),
    name="dowload_data", ignore_result=True)
def dowload_data():
    driver = webdriver.Remote(
        command_executor=DRIVER_PATH,
        desired_capabilities=webdriver.DesiredCapabilities.CHROME
    )
    Dowloader(driver).download()
    driver.close()


@periodic_task(
    run_every=(crontab(
        minute=UPLOAD_SCHEDULE_MINS, hour=UPLOAD_SCHEDULE_HOURS)
    ),
    name="upload_data", ignore_result=True)
def upload_data():
    Uploder().upload()


@periodic_task(
    run_every=(crontab(
        minute=LIKES_SCHEDULE_MINS, hour=LIKES_SCHEDULE_HOURS)
    ),
    name="run_bot", ignore_result=True)
def run_bot():
    Likes(USER, PASSWORD, TAGS_FOR_LIKE, MAX_LIKES).run_round_safe()
