from django.db.models import signals
from django.dispatch import receiver
from django.db import transaction
from django.core.mail import mail_admins
from django.shortcuts import get_object_or_404

from my_homepage.testimonials.models import Testimonial


@receiver(signals.post_save, sender=Testimonial)
def notify_new_testimonial(sender, instance, created, **kwargs):
    '''Notifies admins of new testimonial submission from homepage'''
    if created:
        testimonial = get_object_or_404(Testimonial, id=instance.id)
        name = testimonial.name
        comment = testimonial.comment
        subject = f'[New Testimonial] New testimonial from {name}'
        message = comment
        mail_admins(subject, message=message, fail_silently=False, connection=None, html_message=None)
