from werkzeug.wrappers import CommonResponseDescriptorsMixin
from app import app
from UnleashClient import UnleashClient
from datetime import datetime

client = UnleashClient(url="http://unleash:4242/api",
                       app_name="flask-feature-flag",
                       refresh_interval=2)

client.initialize_client()


@app.route('/')
def hello_world():
    if client.is_enabled("flask-feature-flag"):
        return 'Feature ENABLED'
    else:
        return "Feature is NOT enabled"


@app.route('/api/v1/time')
def api_flag():
    if client.is_enabled("api-v1-time"):

        datetime_json = {
            "datetime": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            "week": datetime.now().strftime("%U"),
        }
        return datetime_json

    else:
        return datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z')
