# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 14:38:32 2023

@author: victor
"""

import sys
import pymongo
from pymongo import MongoClient
from datetime import datetime
mongo_url_01="mongodb://admin:bmwee8097218@140.118.122.115:30415/"
def catch_channelbusy(DB,Collection):
    global mongo_url_01
    try:
        conn = MongoClient(mongo_url_01) 
        db = conn[DB]
        collection = db[Collection]
        cursor=collection.find().sort("_id",-1).limit(45)
        data=[d for d in cursor]
        if data==[]:
            return False
        else:
            return data
    except:
        return False