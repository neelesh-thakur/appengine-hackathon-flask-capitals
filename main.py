import logging

from flask import Flask
from flask_cors import CORS
import api


app = Flask(__name__)
CORS(app)


app.register_blueprint(api.api)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
