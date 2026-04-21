# Metadata: label=MongoDB connection strings in Python, type=database_connection, db_type=mongodb, context=Python code, generator=manual

from pymongo import MongoClient
import os

class DatabaseConfig:
    # Standard MongoDB connection
    MONGO_URI = "mongodb://mongouser:M0ng0P@ss123@mongo.example.com:27017/mydb?authSource=admin"

    # MongoDB Atlas connection (SRV)
    ATLAS_URI = "mongodb+srv://atlasuser:Atl@sP@ssw0rd2024@cluster0.abcd1.mongodb.net/production?retryWrites=true&w=majority"

    # Replica set connection
    REPLICA_URI = "mongodb://admin:R3plic@S3t_P@ss@mongo1.example.com:27017,mongo2.example.com:27017,mongo3.example.com:27017/mydb?replicaSet=rs0&authSource=admin"

    # With all authentication options
    FULL_URI = "mongodb://dbadmin:C0mpl3x_P@ssw0rd!@mongodb.internal.example.com:27017/app_database?authSource=admin&ssl=true&readPreference=primaryPreferred"

def get_client():
    # Environment variable approach
    connection_string = os.getenv(
        'MONGODB_URL',
        'mongodb://devuser:D3v_M0ng0_P@ss@localhost:27017/dev_database'
    )
    return MongoClient(connection_string)

# Multi-line connection string
mongo_connection = (
    "mongodb://service_account:S3rv1c3_Acc0unt_P@ss@"
    "mongo-shard1.example.com:27017/"
    "sharded_database?authSource=admin"
)
