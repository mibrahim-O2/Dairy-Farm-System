from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
from datetime import datetime
import os

# ======================
# FLASK APP
# ======================
app = Flask(__name__)
app.secret_key = "secret123"  # CHANGE TO STRONG SECRET FOR PRODUCTION

# ======================
# LOGIN CREDENTIALS
# ======================
USERNAME = "admin"
PASSWORD = "1234"

# ======================
# DATABASE CONNECTION
# ======================
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# ======================
# STATIC PATHS
# ======================
LOGO_PATH = os.path.join('static', 'images', 'logo.png')
FONT_PATH = os.path.join('static', 'fonts', 'NotoNastaliq-Regular.ttf')

# ======================
# LOGIN REQUIRED DECORATOR
# ======================
def login_required(func):
    def wrapper(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect("/login")
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

# ======================
# LOGIN ROUTE
# ======================
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == USERNAME and password == PASSWORD:
            session["logged_in"] = True
            return redirect("/")
        else:
            error = "Invalid credentials"
    return render_template("login.html", error=error)

# ======================
# LOGOUT ROUTE
# ======================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ======================
# HOME DASHBOARD
# ======================
@app.route("/")
@login_required
def home():
    search = request.args.get("search")
    db = get_db()

    if search:
        vouchers = db.execute(
            "SELECT * FROM vouchers WHERE name LIKE ?",
            ('%' + search + '%',)
        ).fetchall()
    else:
        vouchers = db.execute("SELECT * FROM vouchers").fetchall()

    latest = {}
    for v in vouchers:
        name = v["name"]
        date = datetime.strptime(v["date"], "%Y-%m-%d")
        if name not in latest or date > datetime.strptime(latest[name]["date"], "%Y-%m-%d"):
            latest[name] = v

    customers = list(latest.values())

    month = datetime.now().strftime("%Y-%m")
    report = db.execute(
        "SELECT SUM(amount) as income, SUM(total_milk) as milk FROM vouchers WHERE date LIKE ?",
        (month + "%",)
    ).fetchone()

    income = report["income"] if report["income"] else 0
    milk = report["milk"] if report["milk"] else 0

    return render_template("index.html", customers=customers, income=income, milk=milk)

# ======================
# ADD VOUCHER
# ======================
@app.route("/add_voucher", methods=["POST"])
@login_required
def add_voucher():
    name = request.form["name"]
    date = request.form["date"]
    days = int(request.form["days"])
    rate = float(request.form["rate"])
    daily = float(request.form["daily"])
    extra = float(request.form["extra"])
    used = float(request.form["used"])
    due = float(request.form["due"])

    total_milk = (daily * days) + extra - used
    amount = total_milk * rate
    final_bill = amount + due

    db = get_db()
    db.execute("""
        INSERT INTO vouchers
        (name,date,days,rate,daily,extra,used,due,total_milk,amount,final_bill)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """, (name,date,days,rate,daily,extra,used,due,total_milk,amount,final_bill))
    db.commit()
    return redirect("/")

# ======================
# EDIT VOUCHER
# ======================
@app.route("/edit/<int:id>")
@login_required
def edit(id):
    db = get_db()
    data = db.execute("SELECT * FROM vouchers WHERE id=?", (id,)).fetchone()
    return render_template("edit.html", data=data)

@app.route("/update/<int:id>", methods=["POST"])
@login_required
def update(id):
    name = request.form["name"]
    date = request.form["date"]
    days = int(request.form["days"])
    rate = float(request.form["rate"])
    daily = float(request.form["daily"])
    extra = float(request.form["extra"])
    used = float(request.form["used"])
    due = float(request.form["due"])

    total_milk = (daily * days) + extra - used
    amount = total_milk * rate
    final_bill = amount + due

    db = get_db()
    db.execute("""
        UPDATE vouchers SET
        name=?,date=?,days=?,rate=?,daily=?,extra=?,used=?,due=?,total_milk=?,amount=?,final_bill=?
        WHERE id=?
    """, (name,date,days,rate,daily,extra,used,due,total_milk,amount,final_bill,id))
    db.commit()
    return redirect("/")

# ======================
# DELETE VOUCHER
# ======================
@app.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete(id):
    db = get_db()
    db.execute("DELETE FROM vouchers WHERE id=?", (id,))
    db.commit()
    return redirect("/")

# ======================
# VIEW BILL
# ======================
@app.route("/bill/<int:id>")
@login_required
def bill(id):
    db = get_db()
    data = db.execute("SELECT * FROM vouchers WHERE id=?", (id,)).fetchone()
    return render_template("bill.html", data=data, logo_path=LOGO_PATH, font_path=FONT_PATH)

# ======================
# RUN APP
# ======================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)