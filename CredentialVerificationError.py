#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:05:23 2017

@author: af
"""

class CredentialsVerificationError(Exception):
    
    def __init__(self, message):
        self.message = message