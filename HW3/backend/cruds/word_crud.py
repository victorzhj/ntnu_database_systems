import pymongo
import bson
import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "host": os.getenv("HOST"),
    "port": int(os.getenv("PORT"))
}

mongo_client = pymongo.MongoClient(config["host"], config["port"])
db = mongo_client.local
words_collection = db.words

def get_word(id):
    _id = bson.objectid.ObjectId(id)
    return words_collection.find_one({"_id": _id})

def get_all_words(username):
    return words_collection.find({"username": username})

def insert_new_words(words):
    words_collection.insert_many(words)
    return

def delete_words(ids):
    ids = [bson.objectid.ObjectId(id) for id in ids]
    words_collection.delete_many({"_id": {"$in": ids}})
    return

def modify_word(id, word):
    _id = bson.objectid.ObjectId(id)
    words_collection.update_one({"_id": _id}, {"$set": word})
    return
