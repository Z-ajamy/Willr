import os
from flask import Flask

def create_app(test_conf=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'app.sqlite'))

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
        return "<h1>Hi Willr</h1>"
    
    return app
