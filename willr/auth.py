"""Authentication and authorization module.

This module provides user authentication functionality including registration,
login, logout, and access control through decorators. It handles password
hashing, session management, and user verification.
"""

import functools
from flask import Blueprint, flash, g, url_for, session, request, render_template, redirect
from werkzeug.security import check_password_hash, generate_password_hash
from willr.db import get_db
import sqlite3


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route('/register', methods=("GET", "POST"))
def register():
    """Handle user registration for new accounts.
    
    GET: Displays the registration form.
    POST: Processes registration form submission, validates input, creates new user
    with hashed password, and redirects to login on success.
    
    Returns:
        str: Rendered registration template on GET or validation failure.
        werkzeug.wrappers.Response: Redirect to login page on successful registration.
    
    Raises:
        sqlite3.IntegrityError: If username already exists in database.
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db = get_db()
        err = None
        if not username:
            err = "Username is required"
        elif not password:
            err = "Password is required"
        if not err:
            try:
                db.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, generate_password_hash(password)))
                db.commit()
            except sqlite3.IntegrityError:
                err = f"Username '{username}' is already registered"
            else:
                return redirect(url_for("auth.login"))
        flash(err)
    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Handle user login and authentication.
    
    GET: Displays the login form.
    POST: Processes login form submission, verifies credentials, creates session
    on success, and redirects to index page.
    
    Returns:
        str: Rendered login template on GET or authentication failure.
        werkzeug.wrappers.Response: Redirect to index page on successful login.
    """
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db = get_db()
        err = None
        user = db.execute("SELECT * from user where username = ?", (username,)).fetchone()
        if not user:
            err = f"User '{username}' not found"
        elif not check_password_hash(user["password"], password):
            err = "Incorrect password"
        if not err:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))
        flash(err)
    return render_template("auth/login.html")


@bp.before_app_request
def load_logged_in_user():
    """Load currently logged-in user before each request.
    
    Retrieves user information from the database based on the session's user_id
    and stores it in the g object for access during request processing. If no
    user is logged in, sets g.user to None.
    """
    user_id = session.get("user_id")
    if user_id:
        g.user = get_db().execute("SELECT * from user where id = ?", (user_id,)).fetchone()
    else:
        g.user = None


@bp.route("/logout")
def logout():
    """Handle user logout by clearing the session.
    
    Removes all session data including user_id and redirects to the index page.
    
    Returns:
        werkzeug.wrappers.Response: Redirect to index page after logout.
    """
    session.clear()
    return redirect(url_for("index"))


def login_required(view):
    """Decorator to restrict access to views that require authentication.
    
    Wraps view functions to check if a user is logged in before allowing access.
    Redirects unauthenticated users to the login page.
    
    Args:
        view (function): The view function to wrap with authentication check.
    
    Returns:
        function: Wrapped view function with authentication enforcement.
    
    Examples:
        >>> @login_required
        ... def protected_view():
        ...     return "This requires login"
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not g.user:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view
