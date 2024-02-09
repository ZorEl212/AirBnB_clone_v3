from os import getenv

HBNB_API_HOST = getenv("HBNB_API_HOST")
HBNB_API_PORT = getenv("HBNB_API_PORT")

host = HBNB_API_HOST if HBNB_API_HOST else '0.0.0.0'
port = HBNB_API_PORT if HBNB_API_PORT else 5000