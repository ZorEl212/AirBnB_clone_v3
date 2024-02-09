#!/usr/bin/python3
"""Index page of the web app"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


classes = {'states': 'State', 'cities': 'City', 'users': 'User',
           'palces': 'Place', 'reviews': 'Review','amenities': 'Amenity'}
@app_views.route("/status", strict_slashes=False)
def app_status():
    return jsonify({"status": "OK"})

@app_views.route("/stats", strict_slashes=False)
def stats():
    all_stats = {}
    for key, value in classes.items():
        all_stats[key] = storage.count(value)
    return all_stats
