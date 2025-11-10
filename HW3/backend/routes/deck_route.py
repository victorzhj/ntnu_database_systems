from flask import Blueprint, render_template, request, redirect, url_for, session
from cruds.deck_crud import get_all_decks, create_deck, delete_deck, modify_deck, get_single_deck
from cruds.word_crud import get_word
import bson

deck_route = Blueprint('deck_route', __name__, template_folder='../../frontend/deck_templates')

@deck_route.route('/decks', methods=['GET'])
def show_decks():
    username = session.get('username')
    decks = get_all_decks(username)
    return render_template('decks.html', decks=decks)

@deck_route.route('/show_deck/<deck_id>', methods=['GET'])
def show_deck(deck_id):
    username = session.get('username')
    deck = get_single_deck(deck_id)
    words = []
    for word_id in deck['words']:
        word = get_word(word_id)
        if word and word['username'] == username:
            words.append(word)
    return render_template('show_deck.html', words=words)

@deck_route.route('/addDeck', methods=['POST'])
def add_deck_route():
    username = session.get('username')
    description = request.form.get('description')
    name = request.form.get('name')
    word_ids = [bson.objectid.ObjectId(id) for id in request.form.getlist('word_ids')]
    new_deck = {"description": description, "name": name, "username": username, "words": word_ids}
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