#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:26:15 2017

@author: af
"""

import twitter_manager
import weekdatetime

day = weekdatetime.Weekdatetime().weekday_today()

tManager = twitter_manager.Twitter_manager()
tManager.create_api_instance()
friends = tManager.get_friends()


screen_names = []
for u in friends:
   screen_names.append( "@"+u.screen_name )

for n in screen_names:
    tManager.update('Good morning {0}! It\'s a wonderful {1} today, and I hope you have a wonderful day!'.format(n, day))
    
