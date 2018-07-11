## Getting Started

Open `example.env` and let's check.

`IUSER` - user login (not email!!!)

`IPASSWORD` - user password

`TAGS_FOR_LIKE` - bot will run by this hashtags;

`MAX_LIKES`- how many post you want to like by one hashtag;

`ACCOUNTS` - bot will save photos and video for current date from these accounts and post in to yours;

`MAX_PHOTOS` - how many photos you want to post by one time;

This instruction will get you a copy of the project up and running on your local machine for development and testing purposes.

External resources:

* [1] https://github.com/LevPasha/Instagram-API-python - for upload photo / video

* [2] https://github.com/instabot-py/instabot.py - for likes and etc.

The first repository can give you "following", "liking" users and etc. as the second.
Feel free to fork and improve my code.

Please, do not push directly to repository, fork and have fun!

### Prerequisites

Install docker (docker-compose) on your machine (https://docs.docker.com/install/)

Run from project directory `cp example.env etc/.env`

Open `etc/.env` add your login/password, account, tags and etc.

### Running

```
docker-compose up --build -up
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Legal

This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by Instagram or any of its affiliates or subsidiaries.

This is an independent and unofficial API. Use at your own risk.

## P.S.
Please, follow my [instagram-frenchie-bot](https://www.instagram.com/_myfrenchieamigo_/) :)