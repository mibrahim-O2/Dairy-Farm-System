from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

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
# HOME DASHBOARD
# ======================
@app.route("/")
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

        if name not in latest:
            latest[name] = v
        else:
            old_date = datetime.strptime(latest[name]["date"], "%Y-%m-%d")

            if date > old_date:
                latest[name] = v

    customers = list(latest.values())

    # Monthly report
    month = datetime.now().strftime("%Y-%m")

    report = db.execute(
        "SELECT SUM(amount) as income, SUM(total_milk) as milk FROM vouchers WHERE date LIKE ?",
        (month + "%",)
    ).fetchone()

    income = report["income"] if report["income"] else 0
    milk = report["milk"] if report["milk"] else 0

    return render_template(
        "index.html",
        customers=customers,
        income=income,
        milk=milk
    )


# ======================
# ADD VOUCHER
# ======================
@app.route("/add_voucher", methods=["POST"])
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
def edit(id):

    db = get_db()

    data = db.execute(
        "SELECT * FROM vouchers WHERE id=?",
        (id,)
    ).fetchone()

    return render_template("edit.html", data=data)


@app.route("/update/<int:id>", methods=["POST"])
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
# DELETE
# ======================
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    db = get_db()

    db.execute("DELETE FROM vouchers WHERE id=?", (id,))
    db.commit()

    return redirect("/")


# ======================
# VIEW BILL
# ======================
@app.route("/bill/<int:id>")
def bill(id):

    db = get_db()

    data = db.execute(
        "SELECT * FROM vouchers WHERE id=?",
        (id,)
    ).fetchone()

    return render_template(
        "bill.html",
        data=data,
        logo_path=LOGO_PATH,
        font_path=FONT_PATH
    )


# ======================
# RUN APP
# ======================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)