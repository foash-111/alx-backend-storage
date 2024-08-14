#!/usr/bin/env python3
"""pymongo update"""


def update_topics(mongo_collection, name, topics):
    """update"""
    mongo_collection.update_one({'name': name}, { '$set': {'topics': topics} })
