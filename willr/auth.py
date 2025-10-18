import functools
from flask import Blueprint, flash, g, url_for, session, request, render_template, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from willr.db import get_db
import sqlite3


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route('/register', methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db = get_db()
        err = None
        if not username:
            err = "No username"
        elif not password:
            err = "No password"
        if not err:
            try:
                db.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, generate_password_hash(password)))
                db.commit()
            except sqlite3.IntegrityError:
                err = f"{username} is Exists"
            else:
                return redirect(url_for("auth.login"))
        flash(err)
    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db = get_db()
        err = None
        user = db.execute("SELECT * from user where username = ?", (username)).fetchone()
        if not user:
            err = f"{username} Not Found"
        elif not check_password_hash(user["password"], password):
            err = "Not correct password"
        if not err:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))
        flash(err)
    return render_template("auth/login.html")

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id:
        g.user = get_db().execute("SELECT * from user where id = ?", (user_id)).fetchone()
    else:
        g.user = None


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not g.user:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view
