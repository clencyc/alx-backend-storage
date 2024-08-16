#!/usr/bin/env python3
"""
Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """ Lists all docs in a collection """
    documents = []
    cursor = mongo_collection.find()

    for document in cursor:
        documents.append(document)

    return documents
