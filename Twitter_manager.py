#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:50:37 2017

@author: af
"""

import twitter
from passwords import Keys
import CredentialVerificationError

class Twitter_manager:
    
    def __init__(self):
        self.twitter = twitter
        self.api = None
        self.__consumer_key__ = Keys.CONSUMER_KEY.value
        self.__consumer_key_secret__ = Keys.CONSUMER_KEY_SECRET.value
        self.__access_token__ = Keys.ACCESS_TOKEN_KEY.value
        self.__access_token_secret__ = Keys.ACCESS_TOKEN_SECRET.value
        
    def create_api_instance(self):
        api = self.twitter.Api(consumer_key = self.__consumer_key__,
                          consumer_secret = self.__consumer_key_secret__,
                          access_token_key = self.__access_token__,
                          access_token_secret = self.__access_token_secret__)
        if api.VerifyCredentials() == None:
            raise CredentialVerificationError('Credentials could not be verified.')
            
        self.api = api
        return api
            
    def get_friends(self):
        users = self.api.GetFriends()
        return users
    
    def get_followers(self):
        return self.api.GetFollowerIDs
    
    def update(self, message):
        self.api.PostUpdate(message)