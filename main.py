#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 08:44:58 2017

@author: af
"""

import Twitter_manager
import datetime

date = datetime.datetime.now()

today = date.weekday()

def week(day):
    return {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday",
            }.get(day, "Doomsday")
    
print("Today is {0} and so".format(week(today)))



#tm = Twitter_manager.Twitter_manager()
#api = tm.create_api_instance()
#status = api.PostUpdate('This day is really a #bauta day')

