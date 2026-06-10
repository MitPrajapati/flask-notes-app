from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config['SECRET_KEY'] = 'my-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from routes.auth import auth_bp
    from routes.notes import notes_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(notes_bp)

    return app