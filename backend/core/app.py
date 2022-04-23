# -*- coding: utf-8 -*-
# nekstas-site
from flask import Flask

from backend.views.index_view import IndexView


class App(Flask):
    def __init__(self):
        super().__init__(__name__)
        self.register()

    def register(self):
        IndexView.register(self)

    def run(self, **kwargs):
        super().run(
            host='0.0.0.0',
            port=5000,
            debug=True,
            **kwargs
        )
