from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sjd'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    db.init_app(app)
    from .views import views
    from .auth import auth
    from .github import github_blueprint

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(github_blueprint, url_prefix="/github_login")

    from .models import User, Note
    with app.app_context():
        create_database()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database():
    db_path = os.path.join('instance', DB_NAME)
    if not os.path.exists(db_path):
        db.create_all()
        print('Database created!')
