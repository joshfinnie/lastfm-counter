#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
import twitter
import os
from dotenv import load_dotenv

from collections import OrderedDict

load_dotenv()

API_KEY = os.getenv("API_KEY")
PERIOD = (
    os.getenv("PERIOD") or "7day"
)  # overall | 7day | 1month | 3month | 6month | 12month
LIMIT = (
    os.getenv("LIMIT") or "5"
)  # The number of results to fetch per page. Defaults to 50
USER = os.getenv("LASTFM_USER")

_VERSION_ = "2.0"
_METHOD_ = "user.gettopartists"
_FORMAT_ = "json"

url = "http://ws.audioscrobbler.com/{}/?method={}&user={}&api_key={}&format={}&period={}&limit={}".format(
    _VERSION_, _METHOD_, USER, API_KEY, _FORMAT_, PERIOD, LIMIT
)

response = requests.get(url)
response.raise_for_status()
r = response.json()

output = OrderedDict()
for artist in r["topartists"]["artist"]:
    output[artist["@attr"]["rank"]] = {
        "name": artist["name"],
        "playcount": artist["playcount"],
    }

last_item = len(output) - 1
time_period = ""
if PERIOD == "7day":
    time_period = " 7 days"
elif PERIOD == "1month":
    time_period = " 1 month"
elif PERIOD == "3month":
    time_period = " 3 months"
elif PERIOD == "6month":
    time_period = " 6 months"
elif PERIOD == "12month":
    time_period = " year"
elif PERIOD == "overall":
    time_period = ""

final_str = "♫ My Top {} played artists in the past{}:".format(len(output), time_period)

for i, (_, value) in enumerate(output.items()):
    if i == last_item:
        final_str += " & {} ({}). Via #LastFM ♫".format(
            value["name"], value["playcount"]
        )
    elif i == last_item - 1:
        final_str += " {} ({})".format(value["name"], value["playcount"])
    else:
        final_str += " {} ({}),".format(value["name"], value["playcount"])

print(final_str)

# Tweet
if "--tweet" in sys.argv or "-t" in sys.argv:
    api = twitter.Api(
        consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
        consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
        access_token_key=os.getenv("TWITTER_ACCESS_KEY"),
        access_token_secret=os.getenv("TWITTER_ACCESS_SECRET"),
        input_encoding="utf-8",
    )
    status = api.PostUpdate(final_str)
    print("{0} just posted: {1}".format(status.user.name, status.text))
