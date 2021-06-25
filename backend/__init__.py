import os
from flask import Flask
from .main import MAIN as main_blueprint


def create_app(config_name):
    """This function is for the flask run we initialize
    all configuration like templates folder and static
    folder for the front-end, the DB and the neccesary for
    login.

    :returns: Flask app
    :rtype: Flask
    """
    app = Flask(__name__,
                template_folder='../frontend/templates/',
                static_folder='../frontend/static')

    app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]

    # blueprint for non-auth parts of app
    app.register_blueprint(main_blueprint)

    # app.run(debug=True)
    return app
