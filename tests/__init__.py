import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config[u'DEBUG']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"



def url_exists(url):
    r = requests.get(url)
    if r.status_code == 200:
        return True

    elif r.status_code == 404:
        return False
