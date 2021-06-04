from django.db import models


class NewContact(models.Model):
    '''Model for new contacts from frontend form'''
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(blank=True, max_length=150)
    content = models.CharField(max_length=5000)

    def __str__(self):
        return self.name