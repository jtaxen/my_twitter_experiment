#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:49:53 2017

@author: af
"""

import datetime

class Weekdatetime:
    
    now = datetime.datetime.now()
    
    def weekday_today(self):
        day = self.now.weekday()
        return {
                0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday",
        }.get(day, "Doomsday")      # If self.weekday returns anything else than 0 - 6, then truly something is very wrong