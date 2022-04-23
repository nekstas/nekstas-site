# -*- coding: utf-8 -*-
# nekstas-site
import os

from dotenv import load_dotenv

load_dotenv()

# Режим отладки
DEBUG_MODE = bool(os.environ.get('DEBUG_MODE', False))

# Настройки веб-сервера
SERVER_HOST = '0.0.0.0'
SERVER_PORT = int(os.environ.get('PORT', 8080))
SECRET_KEY = os.environ.get('SECRET_KEY', 'nekstas-secret-key')

# Расположения разных папок и файлов
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '', '..', '..'
))
FRONTEND_FOLDER = os.path.join(PROJECT_ROOT, 'frontend')
STATIC_FOLDER = os.path.join(FRONTEND_FOLDER, 'static')
TEMPLATE_FOLDER = os.path.join(FRONTEND_FOLDER, 'templates')

# Некоторые URL
STATIC_URL_PATH = '/static'

