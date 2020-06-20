from flask import Flask, jsonify
from flask_restx import Api
from elasticsearch import Elasticsearch


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="Nessus API", version="0.1.0")

    register_routes(api, app)

    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
