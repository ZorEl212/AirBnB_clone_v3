#!/usr/bin/python3
"""starting pointthe web app"""

from models import storage
from flask import Flask
from api.v1.views import app_views
from api.v1 import host, port


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)
