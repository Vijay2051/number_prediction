from flask import Flask
from main.config import Config
import os


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from predict.routes import predict

    app.register_blueprint(predict)
    return app
