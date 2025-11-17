from flask import Blueprint, render_template, request, redirect, session, url_for
from cruds.word_crud import get_all_words, insert_new_words, delete_words, modify_word
import json


word_route = Blueprint('word_route', __name__, template_folder='../../frontend/words_templates')

@word_route.route('/words', methods=['GET'])
def show_words():
    return render_template('words.html')

@word_route.route('/getWords', methods=['GET'])
def get_words():
    username = session.get('username')
    words = get_all_words(username)
    for w in words:
        if '_id' in w:
            w['_id'] = str(w['_id'])
    return json.dumps(words)

@word_route.route('/wordAddPage', methods=['GET'])
def word_add_page():
    return render_template('add_word.html', username=session.get('username'))

@word_route.route('/flipcards', methods=['GET'])
def flipcard_page():
    return render_template('flipcard.html')

@word_route.route('/addWords', methods=['POST'])
def add_words_route():
    word_form = request.get_json()
    print(word_form)
    for word in word_form["cards"]:
        word['username'] = session.get('username')
    try:
        insert_new_words(word_form["cards"])
        print("Words added successfully")
        return redirect(url_for('word_route.show_words'))
    except Exception as e:
        print(f"Error adding words: {e}")
        return redirect(url_for('word_route.show_words'))
    
@word_route.route('/deleteWords', methods=['POST'])
def delete_words_route():
    word_form = request.get_json()
    print(word_form)
    try:
        delete_words(word_form["_ids"])
        print("Words deleted successfully")
        return redirect(url_for('word_route.show_words'))
    except Exception as e:
        print(f"Error deleting words: {e}")
        return redirect(url_for('word_route.show_words'))

@word_route.route('/modifyWord', methods=['POST'])
def modify_word_route():
    word_form = request.get_json()
    id = word_form["_id"]
    try:
        modify_word(id, word_form)
        print("Word modified successfully")
        return redirect(url_for('word_route.show_words'))
    except Exception as e:
        print(f"Error modifying word: {e}")
        return redirect(url_for('word_route.show_words'))