from flask import Flask
from flask_restplus import Api
from .score import features, score
from .api import namespace

api = Api(
    title='My Sample API',
    version='1.0',
    description='Flask-Restplus Example',
)

api.namespaces.clear()
api.add_namespace(namespace)

app = Flask(__name__)
api.init_app(app)
