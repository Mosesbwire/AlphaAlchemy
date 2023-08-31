#!/usr/bin/python3

from api.v1.views import app_views
from api.v1.error import BadRequest
from flask import Flask, make_response, jsonify


app = Flask(__name__)

app.url_map.strict_slashes = False

app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Resource not found"}), 404)

@app.errorhandler(BadRequest)
def bad_request(error):
    resp = {"error": error.errors}

    return make_response(jsonify(resp), 400)

if __name__ == "__main__":
    app.run('0.0.0.0', 5000, threaded = True, debug = True)
