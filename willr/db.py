"""Database initialization and connection management module.

This module handles SQLite database connections, provides database initialization
functionality, and registers CLI commands for database management in the Flask application.
"""

import click
import sqlite3
from datetime import datetime
from flask import current_app, g


def get_db():
    """Get the database connection for the current application context.
    
    Creates a new database connection if one doesn't exist in the application
    context (g object). Configures the connection to return Row objects for
    dictionary-like access to query results.
    
    Returns:
        sqlite3.Connection: Active database connection with Row factory configured.
    
    Examples:
        >>> db = get_db()
        >>> cursor = db.execute('SELECT * FROM users')
    """
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES)
    g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    """Close the database connection if it exists.
    
    Removes the database connection from the application context and closes it
    to free up resources. This function is typically called automatically at the
    end of each request.
    
    Args:
        e (Exception, optional): Exception that triggered the teardown, if any.
            Defaults to None.
    """
    db = g.pop("db", None)
    if db:
        db.close()


def init_db():
    """Initialize the database with schema from schema.sql file.
    
    Executes the SQL commands in schema.sql to create all necessary tables
    and initial database structure. This will reset the database if it already exists.
    
    Raises:
        FileNotFoundError: If schema.sql file is not found in the application resources.
    """
    db = get_db()
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))


@click.command('init-db')
def init_db_command():
    """Flask CLI command to initialize the database.
    
    Command-line interface command that calls init_db() and provides user feedback.
    Usage: flask init-db
    """
    init_db()
    click.echo("Database initialized successfully!")


sqlite3.register_converter("timestamp", lambda v: datetime.fromisoformat(v.decode()))


def init_app(app):
    """Register database functions and CLI commands with the Flask application.
    
    Configures the application to automatically close database connections after
    each request and registers the init-db CLI command for database initialization.
    
    Args:
        app (Flask): The Flask application instance to configure.
    
    Examples:
        >>> app = Flask(__name__)
        >>> init_app(app)
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
