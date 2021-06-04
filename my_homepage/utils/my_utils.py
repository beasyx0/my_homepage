import json
import urllib

from io import BytesIO
from django.conf import settings
from django.core.files import File

from PIL import Image


def make_thumbnail(image, size=(500, 500)):
    """Makes thumbnails of given size from given image"""
    im = Image.open(image)
    im = im.convert('RGB') # convert mode
    im.thumbnail(size) # resize image
    thumb_io = BytesIO() # create a BytesIO object
    im.save(thumb_io, 'JPEG', quality=85) # save image to BytesIO object
    resized_image = File(thumb_io, name=image.name) # create a django friendly File object
    return resized_image


def process_recaptcha(request):
    '''Process google recaptcha and returns True for success or False for any other response'''
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    data = urllib.parse.urlencode(values).encode()
    req =  urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())

    if result['success']:
        return True
    else:
        return False
