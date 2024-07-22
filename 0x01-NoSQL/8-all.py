#!/usr/bin/env python3
"""Lists all documents in a collection"""
import pymongo

def list_all(mongo_collection):
    """lists all documents in a collection"""

    docs = []

    for doc in mongo_collection.find():
        docs.append(doc)

    return docs
