from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Stocks(db.Model):

    __tablename__ = "stocks"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.INTEGER)
    symbol = db.Column(db.TEXT)
    name = db.Column(db.TEXT)
    shares = db.Column(db.INTEGER)
    cost = db.Column(db.REAL)

    def __init__(self, user_id, symbol, name, shares, cost):
        self.user_id = user_id
        self.symbol = symbol
        self.name = name
        self.shares = shares
        self.cost = cost