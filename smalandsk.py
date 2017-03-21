#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:18:09 2017

@author: af
"""
import random

class Smalandsk_ortsnamnsgenerator:
    
    def __init(self):
        pass
    
    prefixes = [
            "Väst",
            "Öst",
            "Finn",
            "Sunner",
            "Vär",
            "All",
            "Kinne",
            "Norr",
            "Upp",
            "Kon",
            "Njud",
            "Aspe",
            "Jön",
            "Väx",
            "Kal",
            "Väster",
            "Värna",
            "Näss",
            "Ljung",
            "Tran",
            "Vet",
            "Ny",
            "Gisla",
            "Ek",
            "Älm",
            "Banke",
            "Alve",
            "Vimmer",
            "Linds",
            "Hults",
            "Tju",
            "Säv"]
    
    suffixes = [
            "köping",
            "jö",
            "mar",
            "vik",
            "hult",
            "mo",
            "hamn",
            "sjö",
            "by",
            "ås",
            "landa",
            "bro",
            "ved",
            "sta",
            "dal",
            "fred",
            "bo",
            "ung",
            "ta",
            "torp",
            ]
    
    def generate(self):
        preIndex = random.randint(0,len(self.prefixes) - 1)
        suffIndex = random.randint(0, len(self.suffixes) - 1)
        prefix = self.prefixes[preIndex]
        suffix = self.suffixes[suffIndex]
        return prefix + suffix