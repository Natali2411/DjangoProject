"""
WSGI config for DjangoProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse, Http404
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')

application = get_wsgi_application()


def test_1(request):
    return HttpResponse("Test home page")


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>Через %s часов будет %s.</body></html>" % (offset, dt)
    return HttpResponse(html)