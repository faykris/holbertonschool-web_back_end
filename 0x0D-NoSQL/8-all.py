#!/usr/bin/env python3
"""8. List all documents in Python"""


def list_all(mongo_collection):
    """list_all - function"""
    docs = mongo_collection.find()
    if len(list(docs)) > 0:
        return mongo_collection.find()
    return []
