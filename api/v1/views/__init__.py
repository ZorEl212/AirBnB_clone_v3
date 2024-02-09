#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint("views", __name__, url_prefix='/api/v1')
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {'states': State, 'cities': City, 'users': User,
           'places': Place, 'reviews': Review, 'amenities': Amenity}

from api.v1.views.index import *
from api.v1.views.states import *
