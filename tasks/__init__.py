from celery import Celery
from celery.schedules import crontab
from celery.task import periodic_task

from etc.constants import (
    ACCOUNTS, TAGS_FOR_LIKE, USER, PASSWORD, MAX_LIKES, AMQP_URL, DRIVER_PATH,
    DOWNLOAD_SCHEDULE_HOURS, UPLOAD_SCHEDULE_HOURS, LIKES_SCHEDULE_HOURS,
    DOWNLOAD_SCHEDULE_MINS, LIKES_SCHEDULE_MINS, UPLOAD_SCHEDULE_MINS)
from etc import Dowloader, Likes, Uploder

from selenium import webdriver

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
    downloader = Dowloader(driver)
    [downloader.download(name) for name in ACCOUNTS]
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
