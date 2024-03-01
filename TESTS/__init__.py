from flask import Flask

def create_app():
    app = Flask(__name__)
    #app.config['SECRET_KEY'] = 'ceci est notre secret_key'

    from .views import views
    from .authentification import authentification 

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(authentification, url_prefix = '/authentification/')

    return app
