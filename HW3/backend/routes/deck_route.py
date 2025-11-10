from flask import Blueprint, render_template, request, redirect, url_for
from cruds.deck_crud import get_all_decks, create_deck, delete_deck, modify_deck
import bson

deck_route = Blueprint('deck_route', __name__, template_folder='../../frontend/deck_templates')

@deck_route.route('/decks', methods=['GET'])
def show_decks():
    decks = get_all_decks()
    return render_template('decks.html', decks=decks)

@deck_route.route('/addDeck', methods=['POST'])
def add_deck_route():
    description = request.form.get('description')
    name = request.form.get('name')
    user_id = bson.objectid.ObjectId(request.form.get('user_id'))
    word_ids = [bson.objectid.ObjectId(id) for id in request.form.getlist('word_ids')]
    new_deck = {"description": description, "name": name, "user_id": user_id, "words": word_ids}
    try:
        create_deck(new_deck)
        print("Deck added successfully")
        return redirect(url_for('deck_route.show_decks'))
    except Exception as e:
        print(f"Error adding deck: {e}")

@deck_route.route('/deleteDeck/<deck_id>', methods=['POST'])
def delete_deck_route(deck_id):
    try:
        delete_deck(deck_id)
        print("Deck deleted successfully")
        return redirect(url_for('deck_route.show_decks'))
    except Exception as e:
        print(f"Error deleting deck: {e}")

@deck_route.route('/modifyDeck/<deck_id>', methods=['POST'])
def modify_deck_route(deck_id):
    word_ids = request.form.getlist('word_ids')
    try:
        modify_deck(deck_id, word_ids)
        print("Deck modified successfully")
        return redirect(url_for('deck_route.show_decks'))
    except Exception as e:
        print(f"Error modifying deck: {e}")