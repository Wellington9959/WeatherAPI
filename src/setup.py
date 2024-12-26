from flask import Flask

from src.configuration import AppSettings
from src.limiter import limiter
from src.routes import base


def create_application(settings: AppSettings) -> Flask:
    application = Flask("WeatherAPI")
    application.config.from_object(settings)
    application.register_blueprint(base)
    limiter.init_app(application)

    return application
