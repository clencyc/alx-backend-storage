#!/usr/bin/env python3
"""
Python function that returns the list of school having a specific topics
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of schools having a specific topic
    """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [d for d in documents]
    return list_docs
