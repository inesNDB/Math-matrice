from flask import Flask

def create_app():
    app = Flask(__name__)
    #app.config['SECRET_KEY'] = 'ceci est notre secret_key'
    return app
