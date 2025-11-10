from flask import Blueprint, render_template, request, redirect, url_for
from cruds.word_crud import get_all_words, insert_new_words, delete_words, modify_word
import json


word_route = Blueprint('word_route', __name__, template_folder='../../frontend/templates')

@word_route.route('/words', methods=['GET'])
def show_words():
    words = get_all_words()
    return render_template('words.html', words=words)

@word_route.route('/addWords', methods=['POST'])
def add_words_route():
    word_form = request.get_json()
    try:
        insert_new_words(word_form)
        print("Words added successfully")
        return redirect(url_for('word_route.show_words'))
    except Exception as e:
        print(f"Error adding words: {e}")
        return redirect(url_for('word_route.show_words'))
    
@word_route.route('/deleteWords', methods=['POST'])
def delete_words_route():
    word_form = request.get_json()
    try:
        delete_words(word_form)
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
        modify_word(word_form)
        print("Word modified successfully")
        return redirect(url_for('word_route.show_words'))
    except Exception as e:
        print(f"Error modifying word: {e}")
        return redirect(url_for('word_route.show_words'))