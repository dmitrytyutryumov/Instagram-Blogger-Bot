import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES_DIR = os.path.join(BASE_DIR, 'files/')

# user credentials
USER = os.getenv('IUSER')  # please, set a user login, with email won't work
PASSWORD = os.getenv('IPASSWORD')

# Config for like bot
ACCOUNTS = os.getenv('ACCOUNTS', '').split(',')
TAGS_FOR_LIKE = os.getenv('TAGS_FOR_LIKE', '').split(',')

MAX_PHOTOS = int(os.getenv('MAX_PHOTOS', 2))
MAX_LIKES = int(os.getenv('MAX_LIKES', 60))

# Config for amqp connection
AMQP_URL = os.getenv('AMQP_URL', 'amqp://guest:guest@amqp:5672/')

# Config for selenium connection
DRIVER_PATH = os.getenv('DRIVER_URL', 'http://selenium-hub:4444/wd/hub')

# Config for sqlite connection
DB_URL = os.getenv('DB_URL', 'sqlite+pysqlite:///ibot.db')

# Config for celery tasks
LIKES_SCHEDULE_HOURS = os.getenv('LIKES_SCHEDULE_HOURS', '*/3')
UPLOAD_SCHEDULE_HOURS = os.getenv('UPLOAD_SCHEDULE_HOURS', '*/5')
DOWNLOAD_SCHEDULE_HOURS = os.getenv('DOWNLOAD_SCHEDULE_HOURS', '8, 16, 23')

LIKES_SCHEDULE_MINS = os.getenv('LIKES_SCHEDULE_MINS', 0)
UPLOAD_SCHEDULE_MINS = os.getenv('UPLOAD_SCHEDULE_MINS', 0)
DOWNLOAD_SCHEDULE_MINS = os.getenv('DOWNLOAD_SCHEDULE_MINS', 0)

