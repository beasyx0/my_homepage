from django.db import models
from django.utils import timezone


class Testimonial(models.Model):
    '''Testimonial for homepage'''
    date = models.DateTimeField(editable=False)
    name = models.CharField(max_length=50)
    comment = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = timezone.now()
        return super(Testimonial, self).save(*args, **kwargs)
