import datetime
from pymongo import MongoClient

myclient = MongoClient(host='test_mongodb',
                     port=27017,
                     username='root',
                     password='pass',
                     authSource="admin")
mydb = myclient["viruclust_db"]
mycol = mydb["db_meta"]

mydict = {
        "_id": 'viruclust_db_1',
        "collection_name": "viruclust_db_1",
        "date": datetime.datetime.today()
}

x = mycol.insert_one(mydict)
