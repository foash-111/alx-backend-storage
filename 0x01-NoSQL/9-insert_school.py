#!/usr/bin/env python3
"""insert into mongo collection"""


def insert_school(mongo_collection, **kwargs):
    """read from dictionary and insert into our table (collection)"""
    my_dict = {}
    for k, v in kwargs.items():
        my_dict[k] = v

    mongo_collection.insert_one(my_dict)
    return mongo_collection.find(my_dict, {'_id': 1})
