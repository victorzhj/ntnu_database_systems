import pymongo
import os
import bson
from dotenv import load_dotenv

load_dotenv()

config = {
    "host": os.getenv("HOST"),
    "port": int(os.getenv("PORT"))
}

mongo_client = pymongo.MongoClient(config["host"], config["port"])
db = mongo_client.local
deck_collection = db.decks

def get_all_decks(username):
    return deck_collection.find({"username": username})

def create_deck(deck):
    deck_collection.insert_one(deck)
    return

def delete_deck(deck_id):
    _id = bson.objectid.ObjectId(deck_id)
    deck_collection.delete_one({"_id": _id})
    return

def modify_deck(deck_id, words):
    _id = bson.objectid.ObjectId(deck_id)
    deck_collection.update_one({"_id": _id}, {"$set": {"words": words}})
    return