#!/usr/bin/python3
"""View for State objects that handles all default RestFul API actions"""

from models import storage
from api.v1.views import app_views, classes
from flask import abort, jsonify, request, make_response


@app_views.route("/states", strict_slashes=False, methods=['GET'])
def states():
    statesList = []
    states = storage.all(classes['states'])
    for state in states.values():
        statesList.append(state.to_dict())
    return jsonify(statesList)


@app_views.route("/states/<state_id>", strict_slashes=False, methods=['GET'])
def get_state(state_id):
    state = storage.get(classes['states'], state_id)
    return jsonify(state.to_dict()) if state else abort(404)


@app_views.route("states/<state_id>", strict_slashes=False, methods=["DELETE"])
def del_state(state_id):
    state = storage.get(classes.get('states'), state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route("/states", strict_slashes=False, methods=['POST'])
def create_state():
    if not request.is_json:
        abort(400, "Not a JSON")
    data = request.get_json()
    if 'name' not in data.keys():
        abort(400, 'Missing name')
    new_state = classes['states']()
    new_state.name = data['name']
    storage.new(new_state)
    storage.save()
    return make_response(jsonify(new_state.to_dict()), 201)

@app_views.route("/states/<state_id>", strict_slashes=False, methods=['PUT'])
def update_state(state_id):
    if not request.is_json:
        abort(400, "Not JSON")
    data = request.get_json()
    state = storage.get(classes['states'], state_id)
    bad_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in bad_keys and state is not None:
            setattr(state, key, value)
    storage.save()
    return make_response(jsonify(state.to_dict()), 200) if state else abort(404)
