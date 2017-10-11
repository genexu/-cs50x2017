from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Transactions(db.Model):

    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.INTEGER)
    symbol = db.Column(db.TEXT)
    shares = db.Column(db.TEXT)
    price = db.Column(db.REAL)
    transacted = db.Column(db.DATETIME, default=datetime.datetime.utcnow)


    def __init__(self, user_id, symbol, shares, price, transacted = datetime.datetime.utcnow()):
        self.user_id = user_id
        self.symbol = symbol
        self.shares = shares
        self.price = price
        self.transacted = datetime.datetime.utcnow()