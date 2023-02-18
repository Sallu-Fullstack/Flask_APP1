from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from markupsafe import Markup
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# app.register_blueprint(second, url_prefix = "")
app.secret_key = "Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data', 'users.sqlite3')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=15)


db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values =users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method =="POST":
        session.permanent = True 
        user=request.form["nm"]
        gender =request.form["gender"]
        session["user"]=user
        session["gender"]=gender

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash("Logged in Successfully!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/delete")
def delete():
    if "user" in session:
        user = session["user"]
        found_user = users.query.filter_by(name=user).first()
        if "email" in session:
            email = session["email"]
            found_email = users.query.filter_by(email=email).first()
            db.session.delete(found_email)
            db.session.commit()
        db.session.delete(found_user)
        db.session.commit()
        session.pop("user", None)
        session.pop("email", None)
        flash(Markup('Database Deleted, Please <a href="{}">Login Now</a>.'.format(url_for("login"))))
        return render_template("view.html")
    else:
        flash("Please Login First!")
        return redirect(url_for("login"))
    
@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if "gender" in session:
            gender = session.get("gender")

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name = user).first()
            found_user.email = email
            db.session.commit()
            flash(Markup('Email Saved, <a href="{}">View List</a>.'.format(url_for('view'))))
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email, user = user, gender=gender if "gender" in session else None)
    else:
        flash("You are not logged In!")
        return redirect(url_for("login"))
@app.route("/logout")
def logout():
    flash("You have been Logged Out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

if __name__== "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)