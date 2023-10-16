#!/usr/bin/env python3
"""Manipulate mongodb using pymongo"""

def update_topics(mongo_collection,name,topics):
    """Update the a collection tht matches a certain name in the topics field"""
    fields_to_update = {"name":name}
    data_to_update = {"$set":{"topics":topics}}
    mongo_collection.update_many(fields_to_update,data_to_update)
