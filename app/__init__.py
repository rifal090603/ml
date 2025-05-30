from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"], supports_credentials=True)

from app.ml.capstone import ml_bp

app.register_blueprint(ml_bp)