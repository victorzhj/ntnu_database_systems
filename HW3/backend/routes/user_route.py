from flask import Blueprint, render_template, request, redirect, url_for
from cruds.user_crud import login_user, register_user, delete_user
user_route = Blueprint('user_route', __name__, template_folder='../../frontend/user_templates')

@user_route.route('/', methods=['GET'])
def login_route():
    return render_template('loginPage.html')

@user_route.route('/login', methods=['POST'])
def login_user_route():
    username = request.form['username']
    password = request.form['password']
    if login_user(username, password):
        print("Login successful")
        return redirect(url_for('deck_route.show_decks'))
    else:
        print("Invalid credentials")
        return redirect(url_for('user_route.login_route'))
    
@user_route.route('/registerPage', methods=['GET'])
def register_route():
    return render_template('registerPage.html')

@user_route.route('/register', methods=['POST'])
def register_user_route():
    username = request.form['username']
    password = request.form['password']
    if register_user(username, password):
        print("Registration successful")
        return redirect(url_for('user_route.login_route'))
    else:
        print("Registration failed")
        return redirect(url_for('user_route.register_route'))
    
@user_route.route('/deleteUser/<username>', methods=['POST'])
def delete_user_route(username):
    try:
        delete_user(username)
        print("User deleted successfully")
        return redirect(url_for('user_route.login_route'))
    except Exception as e:
        print(f"Error deleting user: {e}")