"""Blog post management module.

This module provides functionality for creating, reading, updating, and deleting
blog posts. It includes views for displaying posts, creating new posts, editing
existing posts, and removing posts with proper authorization checks.
"""

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from willr.auth import login_required
from willr.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    """Display all blog posts in reverse chronological order.
    
    Retrieves all posts from the database with author information using a SQL JOIN
    and displays them on the index page with the most recent posts first.
    
    Returns:
        str: Rendered index template with list of all blog posts.
    """
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    
    return render_template('blog/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    """Create a new blog post.
    
    GET: Displays the post creation form.
    POST: Validates and saves the new post to the database, associating it with
    the currently logged-in user as the author.
    
    Returns:
        str: Rendered create template on GET or validation failure.
        werkzeug.wrappers.Response: Redirect to index page on successful creation.
    """
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id']) 
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id, check_author=True):
    """Retrieve a blog post by ID and verify author ownership.
    
    Fetches a post from the database with author information and optionally
    verifies that the current user is the author of the post.
    
    Args:
        id (int): The ID of the post to retrieve.
        check_author (bool, optional): Whether to verify that the current user
            is the post author. Defaults to True.
    
    Returns:
        sqlite3.Row: The post record with all fields including author information.
    
    Raises:
        werkzeug.exceptions.NotFound: If the post ID does not exist (404).
        werkzeug.exceptions.Forbidden: If check_author is True and the current
            user is not the post author (403).
    
    Examples:
        >>> post = get_post(1)
        >>> post = get_post(1, check_author=False)
    """
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post with ID {id} does not exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    """Update an existing blog post.
    
    GET: Displays the post editing form pre-filled with existing post data.
    POST: Validates and saves the updated post to the database. Only the post
    author can update their own posts.
    
    Args:
        id (int): The ID of the post to update.
    
    Returns:
        str: Rendered update template on GET or validation failure.
        werkzeug.wrappers.Response: Redirect to index page on successful update.
    
    Raises:
        werkzeug.exceptions.NotFound: If the post ID does not exist (404).
        werkzeug.exceptions.Forbidden: If the current user is not the post author (403).
    """
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    """Delete a blog post.
    
    Permanently removes a post from the database. Only the post author can
    delete their own posts. This action cannot be undone.
    
    Args:
        id (int): The ID of the post to delete.
    
    Returns:
        werkzeug.wrappers.Response: Redirect to index page after deletion.
    
    Raises:
        werkzeug.exceptions.NotFound: If the post ID does not exist (404).
        werkzeug.exceptions.Forbidden: If the current user is not the post author (403).
    """
    get_post(id)
    
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
