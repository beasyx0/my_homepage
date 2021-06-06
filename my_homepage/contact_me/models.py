from django.db import models


class NewContact(models.Model):
    '''Model for new contacts from frontend form'''
    name = models.CharField(max_length=60, help_text='Contact name')
    email = models.EmailField(help_text='Contact email')
    subject = models.CharField(blank=True, max_length=150, help_text='Contact subject')
    content = models.CharField(max_length=5000, help_text='Contact content')

    def __str__(self):
        return self.name
