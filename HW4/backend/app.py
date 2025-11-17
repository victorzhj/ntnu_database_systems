from flask import Flask
from routes.word_route import word_route
from routes.deck_route import deck_route
from routes.user_route import user_route
import os
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

app.register_blueprint(word_route)
app.register_blueprint(deck_route)
app.register_blueprint(user_route)

if __name__ == '__main__':
    app.run(debug=True)