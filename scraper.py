#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
import os
import urllib2

print os.getcwd()
print os.listdir(os.getcwd())
print os.path.dirname(os.getcwd())
print os.path.dirname(os.path.dirname(os.getcwd()))

# if 'MORPH_SECRET' in os.environ:
# os.environ['MORPH_TWITTER_CONSUMER_KEY']
# os.environ['MORPH_TWITTER_CONSUMER_SECRET']
# os.environ['MORPH_TWITTER_ACCESS_TOKEN']
# os.environ['MORPH_TWITTER_ACCESS_TOKEN_SECRET']
 
auth = tweepy.OAuthHandler(os.environ['MORPH_TWITTER_CONSUMER_KEY'], os.environ['MORPH_TWITTER_CONSUMER_SECRET'], secure=True)
auth.set_access_token(os.environ['MORPH_TWITTER_ACCESS_TOKEN'], os.environ['MORPH_TWITTER_ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)
 
data = urllib2.urlopen("https://raw.githubusercontent.com/philipnye/free-school-ofsted-ratings-output-test/master/dummy_tweets.txt")
for line in data:
    print line
    api.update_status(status=line)
    time.sleep(180) #Tweet every 3 minutes
