#!/usr/bin/env python3
"""
"""

def top_students(mongo_collection):
    """
    Returns all students sorted by average score with avscore field
    """

    top_st = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_st
