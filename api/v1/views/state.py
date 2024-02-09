#!/usr/bin/python3
"""View for State objects that handles all default RestFul API actions"""

from models import storage
from api.v1.views import app_views, classes
from flask import abort, jsonify


@app_views.route("/states", strict_slashes=False, methods=['GET'])
def states():
    statesList = []
    states = storage.all(classes['states'])
    for state in states.values():
        statesList.append(state.to_dict())
    return statesList


@app_views.route("/states/<state_id>", strict_slashes=False, methods=['GET'])
def get_state(state_id):
    state = storage.get(classes['states'], state_id)
    return state.to_dict() if state else abort(404)


@app_views.route("states/<state_id>", strict_slashes=False, methods=["DELETE"])
def del_state(state_id):
    state = storage.get(classes.get('states'), state_id)
    storage.delete(state)
    storage.save()
    return jsonify({}) if state else abort(404)