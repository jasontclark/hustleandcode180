#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, sys, time
from random import randint
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

handles = sys.argv[1]
f = open(handles, "r")
h = f.readlines()
f.close()

for handle in h:
  handle = handle.rstrip()
  message = handle + " " + sys.argv[2]
  send = api.update_status(message)
  nap = randint(1,60)
  time.sleep(nap)
