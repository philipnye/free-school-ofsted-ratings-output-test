#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
import os
import urllib2

# auth = tweepy.OAuthHandler(os.environ['MORPH_TWITTER_CONSUMER_KEY'], os.environ['MORPH_TWITTER_CONSUMER_SECRET'])
# auth.set_access_token(os.environ['MORPH_TWITTER_ACCESS_TOKEN'], os.environ['MORPH_TWITTER_ACCESS_TOKEN_SECRET'])
# api = tweepy.API(auth)
 
# data = urllib2.urlopen("https://raw.githubusercontent.com/philipnye/free-school-ofsted-ratings-output-test/master/dummy_tweets.txt")

# for line in data:
#     print line
#     api.update_status(status=line)
#     time.sleep(180) #Tweet every 3 minutes

# import csv
# with open('dummy_tweets.csv', 'rb') as dummy_tweets:
# 	dummy_tweet_reader= csv.reader(dummy_tweets, dialect='excel')
# 	for row in dummy_tweet_reader:
# 		print row


#doesn't work - appear not to be able to write to GitHub-hosted docs in this way

# with open('dummy_tweets.csv', 'wb') as dummy_tweets2:
# 	dummy_tweet_writer = csv.writer(dummy_tweets2)
# 	dummy_tweet_writer.writerow(["5 April 2015"] +["No"]+["Rating"]+ ["New rating - Nottingham University Academy of Science and Technology - requires improvement http://philipnye.github.io/free-school-ofsted-ratings/ http://pic.twitter.com/1LPfQIF7wr"])
# 	dummy_tweet_writer.writerow(["5 April 2015"] +["No"]+["Summary"]+ ["Updated - overall 51 out of 77 open, inspected free schools, or 64%, are rated good or better http://philipnye.github.io/free-school-ofsted-ratings/ http://pic.twitter.com/1LPfQIF7wr"])