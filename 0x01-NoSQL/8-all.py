#!/usr/bin/python3
"""pymongo module"""


def list_all(mongo_collection):
    """function that lists all documents in a collection:"""
    if mongo_collection is not None:
        objs = mongo_collection.find()
        return objs
    return []
