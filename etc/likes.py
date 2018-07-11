# -*- coding: utf-8 -*-
import logging

from instabot import Bot


class Likes(object):
    def __init__(self, username, password, tags, max_likes):
        self.username = username
        self.password = password
        self.tags = tags
        self.max_likes = max_likes

    def run_like_round(self, tag):
        bot = Bot(max_following_to_follow=10000,
                  max_following_to_followers_ratio=100,
                  max_follows_per_day=100,
                  max_likes_per_day=self.max_likes)
        bot.login(username=self.username, password=self.password)
        bot.like_hashtag(tag)
        return True

    def run_round_safe(self):
        for tag in self.tags:
            try:
                return self.run_like_round(tag)
            except:
                logging.exception('Something goes wrong')
