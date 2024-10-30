from flask import Flask
from .controllers import example_controller
from .controllers import WeatherController


def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(example_controller.bp)
    app.register_blueprint(WeatherController.weather_bp)
    return app
