#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
import os

# if 'MORPH_SECRET' in os.environ:
# os.environ['MORPH_TWITTER_CONSUMER_KEY']
# os.environ['MORPH_TWITTER_CONSUMER_SECRET']
# os.environ['MORPH_TWITTER_ACCESS_TOKEN']
# os.environ['MORPH_TWITTER_ACCESS_TOKEN_SECRET']
 
# argfile = str(sys.argv[1])
argfile = "dummy_tweets.txt"
 
CONSUMER_KEY = '1234abcd...'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '1234abcd...'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1234abcd...'#keep the quotes, replace this with your access token
ACCESS_SECRET = '1234abcd...'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(os.environ['MORPH_TWITTER_CONSUMER_KEY'], os.environ['MORPH_TWITTER_CONSUMER_SECRET'])
auth.set_access_token(os.environ['MORPH_TWITTER_ACCESS_TOKEN'], os.environ['MORPH_TWITTER_ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(180)#Tweet every 15 minutes