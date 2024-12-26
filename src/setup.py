from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from src.configuration import AppSettings
from src.routes import base


def create_application(settings: AppSettings) -> Flask:
    application = Flask("WeatherAPI")
    application.config.from_object(settings)
    Limiter(
        get_remote_address,
        app=application,
        default_limits=["200 per day", "50 per hour"],
        storage_uri=application.config["REDIS_URL"],
    )
    application.register_blueprint(base)

    return application
