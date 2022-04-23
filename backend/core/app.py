# -*- coding: utf-8 -*-
# nekstas-site
from flask import Flask

from backend.core import config
from backend.views.index_view import IndexView


class App(Flask):
    def __init__(self):
        super().__init__(__name__)
        self.set_config()
        self.register()

    def set_config(self):
        self.config['SECRET_KEY'] = config.SECRET_KEY

        self.static_url_path = config.STATIC_URL_PATH
        self.static_folder = config.STATIC_FOLDER
        self.template_folder = config.TEMPLATE_FOLDER

    def register(self):
        IndexView.register(self)

    def run(self, **kwargs):
        super().run(
            host=config.SERVER_HOST,
            port=config.SERVER_PORT,
            debug=config.DEBUG_MODE,
            **kwargs
        )
