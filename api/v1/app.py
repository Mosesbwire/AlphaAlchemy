#!/usr/bin/python3

from api.v1.views import app_views
from api.v1.error import BadRequest, AuthenticationFailed
from flask import Flask, make_response, jsonify
from flask_cors import CORS


app = Flask(__name__)

app.url_map.strict_slashes = False
CORS(app, resources = {r"/api/v1/*": {"origins": "*"}})
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Resource not found"}), 404)

@app.errorhandler(BadRequest)
def bad_request(error):
    resp = {"error": error.errors}

    return make_response(jsonify(resp), 400)

@app.errorhandler(AuthenticationFailed)
def authentication_failed(error):
    resp = {"error": error.errors}

    return make_response(jsonify(resp), 401)

if __name__ == "__main__":
    app.run('0.0.0.0', 5001, threaded = True, debug = True)
