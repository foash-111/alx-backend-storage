#!/usr/bin/env python3
"""insert into mongo collection"""


def insert_school(mongo_collection, **kwargs):
    """read from dictionary and insert into our table (collection)"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
