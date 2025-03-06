#__init.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'WIP'  # Encrypt/Secure our cookies and session data of our website

    from .views import views  # We need to register these blueprints in init.py
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    return app


