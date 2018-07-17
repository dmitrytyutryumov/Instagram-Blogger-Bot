from celery import Celery
from celery.schedules import crontab
from celery.task import periodic_task
from selenium import webdriver

from etc import Dowloader, Uploder
from etc.constants import (
    AMQP_URL, DRIVER_PATH, DOWNLOAD_SCHEDULE_HOURS, UPLOAD_SCHEDULE_HOURS,
    DOWNLOAD_SCHEDULE_MINS, UPLOAD_SCHEDULE_MINS
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
