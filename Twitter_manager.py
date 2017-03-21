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
        self.consumer_key = Keys.CONSUMER_KEY.value
        self.consumer_key_secret = Keys.CONSUMER_KEY_SECRET.value
        self.access_token = Keys.ACCESS_TOKEN_KEY.value
        self.access_token_secret = Keys.ACCESS_TOKEN_SECRET.value
        
    def create_api_instance(self):
        api = self.twitter.Api(consumer_key = self.consumer_key,
                          consumer_secret = self.consumer_key_secret,
                          access_token_key = self.access_token,
                          access_token_secret = self.access_token_secret)
        #if api.VerifyCredentials() == None:
        #    raise CredentialVerificationError('Credentials could not be verified.')
            
        return api
            
            