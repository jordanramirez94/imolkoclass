import flask
from flask import request, jsonify
from flask_smorest import Api, Blueprint, abort
from blueprints import authors_blueprint
from blueprints import books_blueprint

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['API_TITLE'] = 'Mi libreria V3 Repo'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = "3.0.2"
app.config['OPENAPI_JSON_PATH'] = "api-spec.json"
app.config['OPENAPI_URL_PREFIX'] = "/"
app.config['OPENAPI_SWAGGER_UI_PATH'] = "/"
app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
api = Api(app)

api.register_blueprint(authors_blueprint.blp)
api.register_blueprint(books_blueprint.blp)
app.run()

# Git fanatic

