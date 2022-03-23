#!/usr/bin/env python3
"""12. Log stats"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    total_logs = nginx_collection.find()
    t_GET = nginx_collection.find({"method": "GET"})
    t_POST = nginx_collection.find({"method": "POST"})
    t_PUT = nginx_collection.find({"method": "PUT"})
    t_PATCH = nginx_collection.find({"method": "PATCH"})
    t_DELETE = nginx_collection.find({"method": "DELETE"})
    t_G_Status = nginx_collection.find({"method": "GET", "path": "/status"})
    print("{} logs".format(len(list(total_logs))))
    print("Methods:")
    print("\tmethod GET: {}".format(len(list(t_GET))))
    print("\tmethod POST: {}".format(len(list(t_POST))))
    print("\tmethod PUT: {}".format(len(list(t_PUT))))
    print("\tmethod PATCH: {}".format(len(list(t_PATCH))))
    print("\tmethod DELETE: {}".format(len(list(t_DELETE))))
    print("{} status check".format(len(list(t_G_Status))))
    t_sorted_ips = nginx_collection.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        },
        {
            "$project": {
                "_id": 0,
                "ip": "$_id",
                "count": 1
            }
        }
    ])
    print("IPs:")
    for ip in t_sorted_ips:
        print("\t{}: {}".format(ip.get('ip'), ip.get('count')))
