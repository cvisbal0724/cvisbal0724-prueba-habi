from flask import Flask
from flask_cors import CORS
from controllers.property import routeProperty

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(routeProperty, url_prefix="/property")

def initializateApp(setting):
    app.config.from_object(setting)
    return app
    