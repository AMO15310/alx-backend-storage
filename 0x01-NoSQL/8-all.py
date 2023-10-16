#!/usr/bin/env python3
"""Using pymongo to manipulate mongodb"""

def list_all(mongo_collection):
    """List all documents"""

    if mongo_collection.find().count() == 0:
        return []
    return mongo_collection.find()
