from frask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
	db.init_app(app)
	app.db = db


class Book(db.Model):
	id = db.Collum(db.Integer, primary_key=True)
	book = db.Collum(db.String(255))
	writer = db.Collum(db.String(255))