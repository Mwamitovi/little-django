# project_name/project_name.py
import os
import sys
from django.conf import settings


DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', 'v^2tywnt=emq3qtj!93+-ngib59a9p(o0_f1m*+43wv%1-@)*+')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# settings
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application


# view
def index(request):
    return HttpResponse('Hello World')


# view
def placeholder(request, width, height):
    return HttpResponse('OK')


# url
urlpatterns = [
    url(r'^$', index,
        name='homepage'),
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder,
        name='placeholder'),
]


# wsgi config
application = get_wsgi_application()


# manage
if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
