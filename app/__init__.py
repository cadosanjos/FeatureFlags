from flask import Flask
from UnleashClient import UnleashClient

app = Flask(__name__)

from app import routes

app.run(debug=True, host='0.0.0.0', port=5000)
