#!/usr/bin/env python3
"""14. Top students"""


def top_students(mongo_collection):
    """top_students - function"""

    return mongo_collection.aggregate(
        [
            {
                "$group": {
                    "_id": "$_id",
                    "name": {"$first": "$name"},
                    "averageScore": {"$avg": "$topics.score"}
                }
            }
        ]
    )
