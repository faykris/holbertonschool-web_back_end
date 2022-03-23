#!/usr/bin/env python3
"""14. Top students"""


def top_students(mongo_collection):
    """top_students - function"""

    return mongo_collection.aggregate(
        [
            {
                "$project": {
                    "_id": "$_id",
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
            },
            {
                "$sort": {
                    "averageScore": -1
                }
            }
        ]
    )
