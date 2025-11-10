import pymongo
import os
import bson
from dotenv import load_dotenv

load_dotenv()

connection_url = os.getenv("CONNECTION_STRING")

mongo_client = pymongo.MongoClient(connection_url)
db = mongo_client.flipcardDB
deck_collection = db.decks

def get_all_decks(username):
    return deck_collection.find({"username": username})

def get_single_deck(deck_id):
    _id = bson.objectid.ObjectId(deck_id)
    return deck_collection.find_one({"_id": _id})

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