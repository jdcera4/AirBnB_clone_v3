#!/usr/bin/python3
"""creating an api"""
from os import getenv
from flask import Flask, make_response, jsonify
from api.v1.views import app_views
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def restart_data(exception):
    """close session so the new data is outputed"""
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    """ Return json page mot found """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(
        host=getenv('HBNB_API_HOST', default='0.0.0.0'),
        port=int(getenv('HBNB_API_PORT', default=5000)),
        threaded=True)
