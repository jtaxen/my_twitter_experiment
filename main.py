#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 08:44:58 2017

@author: af
"""

import twitter_manager
import weekdatetime
import random

day = weekdatetime.Weekdatetime().weekday_today()

tManager = twitter_manager.Twitter_manager()
tManager.create_api_instance()
friends = tManager.get_friends()

screen_names = []

for u in friends:
    screen_names.append( "@"+u.screen_name )

randomFriend = random.randint(0, len(screen_names) - 1)
tManager.update('Hey {0}! It\'s the first {1} of the rest of your life! Carpe diem!'.format(screen_names[randomFriend], day))


#commit this


#tm = twitter_manager.Twitter_manager()
#api = tm.create_api_instance()
#status = api.PostUpdate('This day is really a #bauta day')

