from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()



def createApp():
    app = Flask(__name__, template_folder='/home/labris/PycharmProjects/flaskapp/myproject/project/ui/templates', static_folder='/home/labris/PycharmProjects/flaskapp/myproject/project/ui/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://onur:od99@localhost:5432/flask_db'
    db.init_app(app)
    ma.init_app(app)

    return app

