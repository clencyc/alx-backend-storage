#!/usr/bin/env python3
"""
"""

def top_students(mongo_collection):
    """
    Returns all students sorted by average score with avscore field
    """

    pipeline = [
            {"$unwind": "$scores"},
            {"$group": {"_id": "$_id", "name": {"$first": "$name"}, "averageScore": {"$avg": "$scores.score"}}},
            {"$sort": {"averageScore": -1}}
            ]
    result = mongo_collection.aggregate(pipeline)
    return list(result)
