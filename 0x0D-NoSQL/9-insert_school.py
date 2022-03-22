#!/usr/bin/env python3
"""9. Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """insert_school - function"""
    d_doc = {}
    for key, value in kwargs.items():
        d_doc[key] = value
    doc = mongo_collection.insert_one(
        d_doc
    )
    return doc.inserted_id
