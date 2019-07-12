# project_name/project_name.py
import os
import sys
import hashlib
from io import BytesIO
from PIL import Image, ImageDraw
from django.conf import settings


BASE_DIR = os.path.dirname(__file__)

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
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
    ),
    TEMPLATE_DIRS=(
        os.path.join(BASE_DIR, 'templates'),
    ),
    STATICFILES_DIRS=(
        os.path.join(BASE_DIR, 'static'),
    ),
    STATIC_URL = '/static/',
)


from django import forms
from django.conf.urls import url
from django.core.cache import cache
from django.views.decorators.http import etag
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.wsgi import get_wsgi_application


# form
class ImageForm(forms.Form):
    """ validate requested placeholder image."""

    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)

    def generate(self, image_format='PNG'):
        """
        Generate an image of the given type and return as raw bytes.
        """
        width = self.cleaned_data['width']
        height = self.cleaned_data['height']
        _key = '{}.{}.{}'.format(width, height, image_format)

        # check if image is in cache
        _content = cache.get(_key)

        # if data not in cache
        if _content is None:
            _image = Image.new('RGB', (width, height))

            # using ImageDraw to generate text
            draw = ImageDraw.Draw(_image)
            text = '{} X {}'.format(width, height)
            text_width, text_height = draw.textsize(text)

            # add a text overlay if it fits
            if text_width < width and text_height < height:
                text_top = (height - text_height) // 2
                text_left = (width - text_width) // 2
                draw.text((text_left, text_top), text, fill=(255, 255, 255))

            _content = BytesIO()
            _image.save(_content, image_format)
            _content.seek(0)

            # cache image for an hour
            cache.set(_key, _content, 60*60)

        return _content


# view
def index(request):
    return HttpResponse('Hello World')


def generate_etag(request, width, height):
    """ create string representing Etag for image resource """

    _content = 'Placeholder: {0} x {1}'.format(width, height)
    return hashlib.sha1(_content.encode('utf-8')).hexdigest()


# conditional view
@etag(generate_etag)
def placeholder(request, width, height):
    form = ImageForm({'width': width, 'height': height})

    if form.is_valid():
        # generate image of requested size
        _image = form.generate()
        return HttpResponse(_image, content_type='image/png')
    else:
        return HttpResponseBadRequest('Invalid Image Request')


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
