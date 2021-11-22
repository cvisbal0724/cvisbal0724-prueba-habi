from flask import Flask
from flask_cors import CORS
from controllers.property import routeProperty
from .config import setting

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(routeProperty, url_prefix="/")

def initializateApp(setting):
    app.config.from_object(setting)
    return app
    
app = initializateApp(setting['development'])