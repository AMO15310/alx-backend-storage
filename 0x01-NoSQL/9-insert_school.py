#!/usr/bin/env python3
"""Manipulate mongo db using pymongo"""

def insert_school(mongo_collection,**kwargs):
    """Inserts a new document"""
    return mongo_collection.insert(kwargs)
