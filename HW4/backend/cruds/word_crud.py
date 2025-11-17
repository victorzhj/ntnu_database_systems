import pymongo
import bson
import os
from dotenv import load_dotenv

load_dotenv()

connection_string = os.getenv("CONNECTION_STRING")

mongo_client = pymongo.MongoClient(connection_string)
db = mongo_client.flipcardDB
words_collection = db.words

def get_word(id):
    _id = bson.objectid.ObjectId(id)
    return words_collection.find_one({"_id": _id})

def get_all_words(username):
    return list(words_collection.find({"username": username}))

def insert_new_words(words):
    words_collection.insert_many(words)
    return

def delete_word(id):
    words_collection.delete_one({"_id": bson.objectid.ObjectId(id)})
    return

def delete_words(ids):
    words_collection.delete_many({"_id": {"$in": [bson.objectid.ObjectId(id) for id in ids]}})
    return

def modify_word(id, word):
    _id = bson.objectid.ObjectId(id)
    word.pop("_id", None) 
    result = words_collection.update_one({"_id": _id}, {"$set": word})
    print(result)
    return
