from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):

    __tablename__ = "users"
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.TEXT)
    hash = db.Column(db.TEXT)
    cash = db.Column(db.NUMERIC(asdecimal=False), default = 10000)

    def __init__(self, username, hash, cash = 10000):
        self.username = username
        self.hash = hash
        self.cash = cash