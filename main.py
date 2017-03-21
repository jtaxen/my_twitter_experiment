#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 08:44:58 2017

@author: af
"""

class Constants:
    
    def __init__(self):
        self.Twitter = None
        
    def makedir(self, **kwargs):
        self.Twitter = kwargs
    

c = Constants()
c.makedir( green = 2, red = 1, blue = 4)

print(c.Twitter)


print( c.Twitter.get('white','not found'))    