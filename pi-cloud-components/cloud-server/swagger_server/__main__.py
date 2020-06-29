#!/usr/bin/env python3
from typing import Any

import connexion
from connexion import FlaskApp
from swagger_server import encoder
from flask import g, make_response, request

from swagger_server.logic.log_configurator import get_logger

# setup logging so that we don't get spam in stackdriver
logger = get_logger()


def create_app() -> FlaskApp:
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Van Tracker Piside'})

    # Profiling boilerplate
    #
    # @app.app.before_request
    # def before_request():
    #     if "profile" in request.args:
    #         from pyinstrument import Profiler
    #         g.profiler = Profiler()
    #         g.profiler.start()
    #
    # @app.app.after_request
    # def before_request(response):
    #     if not hasattr(g, "profiler"):
    #         return response
    #     g.profiler.stop()
    #     output_html = g.profiler.output_html()
    #     return make_response(output_html)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=8080)
