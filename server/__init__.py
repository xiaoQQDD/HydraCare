"""app module"""
import os
import datetime as dt
from flask import Flask, render_template

from . import auth
from . import rest





def create_app(test_config=None):
    """create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=b'_lkdiokHlkjl*eoiZKLGUIkreiuh' +
        str(dt.datetime.now()).encode('utf-8'),
        DATABASE=os.path.join(app.instance_path, 'sqlite3.db'),
        SQLALCHEMY_DATABASE_URI="sqlite:///" +
        os.path.join(app.instance_path, 'sqlite3.db'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # dbal.init_app(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template('500.html'), 500

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    app.debug = True

    app.register_blueprint(auth.bp)

    app.register_blueprint(rest.bp)
    # app.add_url_rule('/', endpoint='index')

    return app
