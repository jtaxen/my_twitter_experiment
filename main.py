#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 08:44:58 2017

@author: af
"""

import twitter_manager
import weekdatetime
import random
import smalandsk

day = weekdatetime.Weekdatetime().weekday_today()
nameGenerator = smalandsk.Smalandsk_ortsnamnsgenerator()

tManager = twitter_manager.Twitter_manager()
tManager.create_api_instance()
friends = tManager.get_friends()

screen_names = []

for u in friends:
    screen_names.append( "@"+u.screen_name )

randomFriend = random.randint(0, len(screen_names) - 1)
tManager.update('Om du, {0}, tänker bygga en ny by i Småland, så kan den heta {1}. #småland #ortsnamn #ortsnamnsgeneratorn'.format(screen_names[randomFriend], nameGenerator.generate()))


#commit this


#tm = twitter_manager.Twitter_manager()
#api = tm.create_api_instance()
#status = api.PostUpdate('This day is really a #bauta day')

