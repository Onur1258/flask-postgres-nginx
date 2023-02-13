from project import db


def createDB(app):
    with app.app_context():
        db.create_all()

    return db
