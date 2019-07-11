# hello.py
import sys
from django.conf import settings


# settings
settings.configure(
    DEBUG=True,
    SECRET_KEY='wewillwewillrocku',
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


# url
urlpatterns = [
    url(r'^$', index)
]


# wsgi config
application = get_wsgi_application()


# manage
if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
