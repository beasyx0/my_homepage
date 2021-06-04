from PIL import Image
from django.db import models

from my_homepage.utils.my_utils import make_thumbnail

from phone_field import PhoneField
from tinymce import HTMLField


class About(models.Model):
    '''Model to hold information about yourself for homepage'''
    pic = models.ImageField(upload_to='pics', default='default-img.jpg', help_text='Profile picture')
    name = models.CharField(max_length=50, unique=True, help_text='First and last name')
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(blank=True, help_text='Contact email address')
    github_link = models.URLField(blank=True, help_text='Link to your GitHub profile')
    location = models.CharField(blank=True, max_length=50)
    about = HTMLField(help_text='Everything about yourself')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.pic = make_thumbnail(self.pic)
        return super(About, self).save(*args, **kwargs)
