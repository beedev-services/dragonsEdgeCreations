# """
# WSGI config for dragonsEdge project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dragonsEdge.settings')

# # Set script name for the PATH_INFO fix below
# SCRIPT_NAME = os.getcwd()

# class PassengerPathInfoFix(object):
#     """
#         Sets PATH_INFO from REQUEST_URI because Passenger doesn't provide it.
#     """
#     def __init__(self, app):
#         self.app = app

#     def __call__(self, environ, start_response):
#         from urllib.parse import unquote
#         environ['SCRIPT_NAME'] = SCRIPT_NAME
#         request_uri = unquote(environ['REQUEST_URI'])
#         script_name = unquote(environ.get('SCRIPT_NAME', ''))
#         offset = request_uri.startswith(script_name) and len(environ['SCRIPT_NAME']) or 0
#         environ['PATH_INFO'] = request_uri[offset:].split('?', 1)[0]
#         return self.app(environ, start_response)

# # Set the application
# application = get_wsgi_application()
# application = PassengerPathInfoFix(application)

"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dragonsEdge.settings')

application = get_wsgi_application()
