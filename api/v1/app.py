#!/usr/bin/python3
"""starting pointthe web app"""

from models import storage
from flask import Flask, make_response, jsonify
from api.v1.views import app_views
from api.v1 import host, port


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True, debug=True)
