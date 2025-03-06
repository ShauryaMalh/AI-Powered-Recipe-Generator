#__init.py
from flask import Flask, app

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'WIP' #Encrypt/Secure our cookies and session data of our website

    return app


