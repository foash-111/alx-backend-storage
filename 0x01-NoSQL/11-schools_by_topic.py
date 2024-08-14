#!/usr/bin/env python3
"""$in mongodb"""
def schools_by_topic(mongo_collection, topic):
    """find with $in"""
    return mongo_collection.find({ 'topics': {'$in': [topic]} })
