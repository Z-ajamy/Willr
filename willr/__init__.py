"""Flask application factory module.

This module contains the application factory function that creates and configures
the Flask application instance with all necessary extensions, blueprints, and routes.
"""

import os
from flask import Flask


def create_app(test_conf=None):
    """Create and configure the Flask application instance.
    
    This factory function initializes a Flask application with default configuration,
    database setup, authentication, and blog functionality. It supports both production
    and testing configurations.
    
    Args:
        test_conf (dict, optional): Configuration dictionary for testing environment.
            If provided, overrides default configuration. If None, loads from config.py.
            Defaults to None.
    
    Returns:
        Flask: Configured Flask application instance ready to run.
    
    Examples:
        >>> app = create_app()
        >>> app = create_app(test_conf={'TESTING': True, 'DATABASE': ':memory:'})
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'willr.sqlite')
    )

    if test_conf:
        app.config.from_mapping(test_conf)
    else:
        app.config.from_pyfile("config.py", silent=True)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hi")
    def hi():
        """Simple greeting endpoint for testing application functionality.
        
        Returns:
            str: HTML heading with greeting message.
        """
        return "<h1>Hello from Willr!</h1>"
    
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    
    app.add_url_rule('/', endpoint='index')
    
    return app
