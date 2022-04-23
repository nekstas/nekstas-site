# -*- coding: utf-8 -*-
# nekstas-site
from flask_classful import FlaskView, route


class IndexView(FlaskView):
    route_base = '/'

    @route('/')
    def index(self):
        return 'Привет, nekstas.ru! =)'
