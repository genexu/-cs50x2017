from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
from helpers import *

from db_models.users import Users
from db_models.transactions import Transactions
from db_models.stocks import Stocks

# configure application
app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finance.db"
app.config["SQLALCHEMY_ECHO"] = True
sql_alchemy_db = SQLAlchemy(app)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    user_id = session.get("user_id")
    # user_cash = db.execute("SELECT cash from users WHERE id = :id", id = user_id)[0]["cash"]
    user_cash = sql_alchemy_db.session.query(Users.cash).filter(Users.id == user_id).scalar()

    if request.method == "POST":
        input_symbol = request.form.get("symbol")
        input_shares = int(request.form.get("shares"))
        stock = lookup(input_symbol)
        total = input_shares * stock["price"]

        if request.form.get("action") == "buy":
            if user_cash < total:
                return apology("can't afford")

            transaction("buy", input_symbol, input_shares)

        if request.form.get("action") == "sell":
            # user_stock = db.execute("SELECT * FROM stocks WHERE user_id = :user_id AND symbol = :symbol", user_id = user_id, symbol = input_symbol)
            user_stock = Stocks.query.filter(Stocks.user_id == user_id, Stocks.symbol == input_symbol).first()
            # if len(user_stock) == 0 or user_stock[0]["shares"] < input_shares:
            #     return apology("can't afford")
            if not user_stock or user_stock.shares < input_shares:
                return apology("can't afford")

            transaction("sell", input_symbol, input_shares)
        return redirect(url_for("index"))

    # stocks = db.execute("SELECT * from stocks WHERE user_id = :user_id", user_id = user_id)
    stocks = Stocks.query.filter(Stocks.user_id == user_id).all()
    property_sum = user_cash
    for stock in stocks:
        # stock["price"] = lookup(stock["symbol"])["price"]
        stock.price = lookup(stock.symbol)["price"]
        # property_sum += stock["price"] * stock["shares"]
        property_sum += stock.price * stock.shares

    return render_template("portfolio.html", stocks = stocks, cash = user_cash, property_sum = property_sum)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""

    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("missing symbol")
        input_symbol = request.form.get("symbol")
        input_shares = int(request.form.get("shares"))
        stock = lookup(input_symbol)

        if not stock or stock == None:
            return apology("invalid symbol")
        user_id = session.get("user_id")
        total_buy = input_shares * stock["price"]

        # user_cash = db.execute("SELECT cash FROM users WHERE id = :id", id = user_id)[0]["cash"]
        user_cash = sql_alchemy_db.session.query(Users.cash).filter(Users.id == user_id).scalar()
        if user_cash < total_buy:
            return apology("can't afford")

        transaction("buy", input_symbol, input_shares)

        return redirect(url_for("index"))
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions."""

    user_id = session.get("user_id")
    # transactions = db.execute("SELECT * from transactions WHERE user_id = :user_id", user_id = user_id)
    transactions = Transactions.query.filter(Transactions.user_id == user_id)

    return render_template("history.html", transactions = transactions)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        # rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        user = Users.query.filter(Users.username == request.form.get("username")).first()

        # ensure username exists and password is correct
        # if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
        #     return apology("invalid username and/or password")
        if not user or not pwd_context.verify(request.form.get("password"), user.hash):
            return apology("invalid username and/or password")

        # remember which user has logged in
        # session["user_id"] = rows[0]["id"]
        session["user_id"] = user.id

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        if request.form.get("symbol"):
            stack = lookup(request.form.get("symbol"))
            return render_template("quote.html", stack=stack)
        else:
            return apology("missing symbol")
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""

    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username")
        elif not request.form.get("password"):
            return apology("must provide password")
        elif not request.form.get("password_again"):
            return apology("must double check your password")

        if request.form.get("password") != request.form.get("password_again"):
            return apology("make sure that your password and password(again) is equal")

        # rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        rows = Users.query.filter(Users.username == request.form.get("username")).all()

        if len(rows) != 0:
            return apology("username taken")

        hashpwd = pwd_context.hash(request.form["password"])
        # db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
        #     username=request.form["username"], hash=hashpwd)
        new_user = Users(request.form["username"], hashpwd)
        sql_alchemy_db.session.add(new_user)
        sql_alchemy_db.session.commit()

        # rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        user = Users.query.filter(Users.username == request.form.get("username")).first()

        # session["user_id"] = rows[0]["id"]
        session["user_id"] = user.id

        return redirect(url_for("index"))
    else:
        return  render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""

    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("missing symbol")
        input_symbol = request.form.get("symbol")
        input_shares = int(request.form.get("shares"))
        stock = lookup(input_symbol)

        if not stock or stock == None:
            return apology("invalid symbol")

        user_id = session.get("user_id")

        # user_stock = db.execute("SELECT * FROM stocks WHERE user_id = :user_id AND symbol = :symbol", user_id = user_id, symbol = input_symbol)
        user_stock = Stocks.query.filter(Stocks.user_id == user_id, Stocks.symbol == input_symbol).first()

        # if len(user_stock) == 0 or user_stock[0]["shares"] < input_shares:
        if not user_stock or user_stock.shares < input_shares:
            return apology("can't afford")

        transaction("sell", input_symbol, input_shares)

        return redirect(url_for("index"))
    else:
        return render_template("sell.html")

@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    if request.method == "POST":
        if not request.form.get("old_password"):
            return apology("must provide old password")

        if not request.form.get("new_password"):
            return apology("must provide new password")

        if not request.form.get("new_password_again"):
            return apology("must double check your new password")

        if request.form.get("new_password") != request.form.get("new_password_again"):
            return apology("make sure that your new password and new password(again) is equal")

        user_id = session.get("user_id")
        # user = db.execute("SELECT * FROM users WHERE id = :id", id = user_id)
        user = sql_alchemy_db.session.query(Users).filter(Users.id == user_id).first()

        # if not pwd_context.verify(request.form.get("old_password"), user[0]["hash"]):
        if not pwd_context.verify(request.form.get("old_password"), user.hash):
            return apology("invalid old password")

        new_hashpwd = pwd_context.hash(request.form["new_password"])

        # db.execute("UPDATE users SET hash = :new_hash WHERE id = :id", new_hash = new_hashpwd, id = user_id)
        user.hash = new_hashpwd
        sql_alchemy_db.session.commit()

        session.clear()

        return redirect(url_for("login"))
    else:
        return render_template("change_password.html")

@app.route("/add-cash", methods=["GET", "POST"])
@login_required
def add_cash():
    if request.method == "POST":
        amount = float(request.form.get("amount"))
        if not amount:
            return apology("must provide amount")

        user_id = session.get("user_id")

        cash = db.execute("SELECT cash from users WHERE id = :id", id = user_id)[0]["cash"]
        db.execute("UPDATE users SET cash = :new_cash WHERE id = :id", new_cash = cash + amount, id = user_id)

        return redirect(url_for("index"))
    else:
        return render_template("add_cash.html")

def transaction(action_type, symbol, shares):
    user_id = session.get("user_id")
    stock = lookup(symbol)
    total = shares * stock["price"]

    # user_stock = db.execute("SELECT * from stocks WHERE user_id = :user_id AND symbol = :symbol", user_id = user_id, symbol = symbol)
    user_stock = sql_alchemy_db.session.query(Stocks).filter(Stocks.user_id == user_id, Stocks.symbol == symbol).first()
    d_cash, d_shares, d_cost = total, shares , total

    if action_type == "buy": d_cash  = -d_cash
    if action_type == "sell": d_shares, d_cost = -d_shares, -d_cost

    # user_cash = db.execute("SELECT cash FROM users WHERE id = :id", id = user_id)[0]["cash"]
    # db.execute("UPDATE users SET cash = :new_cash WHERE id = :id", new_cash = user_cash + d_cash, id = user_id)
    user = sql_alchemy_db.session.query(Users).filter(Users.id == user_id).first()
    user.cash = user.cash + d_cash
    sql_alchemy_db.session.commit()

    # db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
    #     user_id = user_id, symbol = symbol, shares = shares, price = stock["price"])
    new_transaction = Transactions(user_id, symbol, shares, stock["price"])
    sql_alchemy_db.session.add(new_transaction)
    sql_alchemy_db.session.commit()

    # if action_type == "buy" and len(user_stock) == 0:
    if action_type == "buy" and not user_stock:
        # db.execute("INSERT INTO stocks (user_id, symbol, name, shares, cost) VALUES (:user_id, :symbol, :name, :shares, :cost)",
        #     user_id = user_id, symbol = stock["symbol"], name = stock["name"], shares = shares, cost = stock["price"])
        new_stock = Stocks(user_id, stock["symbol"], stock["name"], shares, stock["price"])
        sql_alchemy_db.session.add(new_stock)
        sql_alchemy_db.session.commit()
    # elif action_type == "sell" and user_stock[0]["shares"] == shares:
    elif action_type == "sell" and user_stock.shares == shares:
        # db.execute("DELETE FROM stocks WHERE id = :id", id = user_stock[0]["id"])
        sql_alchemy_db.session.query(Stocks).filter(Stocks.id == user_stock.id).delete()
        sql_alchemy_db.session.commit()
    else:
        # original_property = user_stock[0]["cost"] * user_stock[0]["shares"]
        # new_stock_shares = user_stock[0]["shares"] + d_shares
        original_property = user_stock.cost * user_stock.shares
        new_stock_shares = user_stock.shares + d_shares

        new_stock_cost = float("{0:.4f}".format((original_property + d_cost) / new_stock_shares))

        # db.execute("UPDATE stocks SET shares = :new_shares, cost = :new_cost WHERE id = :id",
        #     new_shares = new_stock_shares, new_cost = new_stock_cost, id = user_stock[0]["id"])
        user_stock.shares = new_stock_shares
        user_stock.cost = new_stock_cost
        sql_alchemy_db.session.commit()
