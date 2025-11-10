import pymongo
import os

from dotenv import load_dotenv

load_dotenv()

config = {
    "host": os.getenv("HOST"),
    "port": int(os.getenv("PORT"))
}

mongo_client = pymongo.MongoClient(config["host"], config["port"])
db = mongo_client.local
user_collection = db.users

def login_user(username, password):
    user = user_collection.find_one({"username": username, "password": password})
    if not user:
        return False
    return True

def register_user(username, password):
    user = user_collection.find_one({"username": username})
    if user:
        return False
    user_collection.insert_one({"username": username, "password": password})
    return True

def delete_user(username):
    user_collection.delete_one({"username": username})
    return