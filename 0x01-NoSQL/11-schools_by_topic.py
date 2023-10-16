#!/usr/bin/env python3
"""Manipulte mongo db using pymongo"""

def schools_by_topic(mongo_collection,topic):
    """Return a list of content with specific topic"""
    return[mongo_collection.find({"topics":topic})]
