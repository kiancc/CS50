import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    stocks = db.execute("SELECT SUM(shares) as shares, symbol, name, price FROM purchases WHERE user_id = ? GROUP BY name HAVING SUM(shares) > 0", session["user_id"])
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]
    current_stock_info = []
    total_amount = 0

    for stock in stocks:
        stock_info = lookup(stock["symbol"])
        stock_info["shares"] = stock["shares"]
        total_amount += stock_info["shares"] * stock_info["price"]
        current_stock_info.append(stock_info)

    return render_template("/index.html", portfolio=current_stock_info, user=user, total_amount=total_amount)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        data = lookup(request.form.get("symbol"))
        user_info = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]
        shares = request.form.get("shares")

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide stock to buy", 403)

        # Ensure stock exists
        elif not data:
            return apology("stock does not exist", 403)

        # Ensure shares was submitted
        elif not shares:
            return apology("must provide amount of shares to buy", 403)

        # Ensure shares is not negative
        elif int(shares) < 0:
            return apology("share amount cannot be negative")

        # Check if user has enough cash to purchase
        elif user_info["cash"] < data["price"] * int(shares):
            return apology("not enough cash for this transaction")

        else:
            db.execute("INSERT  INTO purchases (user_id, shares, symbol, price, name) VALUES (?, ?, ?, ?, ?)", session["user_id"], int(shares), request.form.get("symbol"), data["price"], data["name"])
            db.execute("UPDATE users SET cash = ? WHERE id = ?", user_info["cash"] - data["price"] * int(shares), session["user_id"])

        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    history = db.execute("SELECT * FROM purchases WHERE user_id = ?", session["user_id"])

    return render_template("/history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide stock", 400)
        else:
            data = lookup(request.form.get("symbol"))

            # Display stock quoted
            return render_template("quoted.html", data=data)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username does not exist, otherwise inserts new user into the database
        if len(rows) == 1:
            return apology("user exists", 400)
        else:
            password_hash = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), password_hash)

        # Redirect user to homepage
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    symbol = db.execute("SELECT symbol FROM purchases WHERE user_id = ? GROUP BY name", session["user_id"])

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        symbol = request.form.get("symbol").split("'")[3]
        data = lookup(symbol)
        user_info = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])[0]
        shares = int(request.form.get("shares"))

        if not request.form.get("shares"):
            return apology("please enter share amount", 403)

        elif int(request.form.get("shares")) < 0:
            return apology("share amount cannot be less than 0", 403)

        else:
            db.execute("INSERT INTO purchases (user_id, shares, symbol, price, name) VALUES (?, ?, ?, ?, ?)", session["user_id"], -shares, symbol, data["price"], data["name"])
            db.execute("UPDATE users SET cash = ? WHERE id = ?", user_info["cash"] + data["price"] * shares, session["user_id"])
            return redirect("/")

    else:
        return render_template("sell.html", symbol=symbol)
