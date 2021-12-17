db = db.getSiblingDB("viruclust_db");
db.viruclust_db_0.drop();
db.db_meta.drop();

db.viruclust_db_0.insertMany([
    {
        "_id": 1,
        "name": "Lion",
        "type": "wild"
    },
    {
        "_id": 2,
        "name": "Cow",
        "type": "domestic"
    },
    {
        "_id": 3,
        "name": "Tiger",
        "type": "wild"
    },
]);

db.db_meta.insertMany([
    {
        "_id": 'viruclust_db_0',
        "collection_name": "viruclust_db_0",
        "date": new Date()
    },
]);