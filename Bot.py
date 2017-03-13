'''
Created on Mar 13, 2017

@author: Daniel McMahon
'''

import tweepy, time, sys

argfile = str(sys.argv[1])

#Insert personal Twitter API keys here
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

filename = open(argfile, "r")
f = filename.readlines()
filename.close

for line in f:
    api.update_status(line)
    time.sleep(900)