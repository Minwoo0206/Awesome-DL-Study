from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY="1q2w3e4r",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHECMY_ECHO = True,
        WTF_CSRF_SECRET_KEY="1q2w3e4r"
    )

    # CSRF와 앱을 연계한다
    csrf.init_app(app)
    # SQLAlchemy와 앱을 연계한다
    db.init_app(app)
    # Migrate와 앱을 연계한다
    Migrate(app, db)

    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    return app

