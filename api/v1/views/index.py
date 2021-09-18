#!/usr/bin/python3
"""creating an api"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status_api():
    return jsonify({"status": "OK"})

@app_views.route("/stats")
def stats():
    """ Return stats objects """
    return jsonify({
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    })
