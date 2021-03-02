from flask import Flask
from UnleashClient import UnleashClient
app = Flask(__name__)


@app.route('/')
def hello_world():
    if client.is_enabled("flask-feature-flag"):
        return 'Feature ENABLED'
    else:
        return "Feature is NOT enabled"

if __name__ == '__main__':
    client = UnleashClient("http://unleash:4242/api", "flask-feature-flag")
    client.initialize_client()
    app.run(debug=True, host='0.0.0.0', port=5000)
