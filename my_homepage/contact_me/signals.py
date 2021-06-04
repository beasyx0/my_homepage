from django.db.models import signals
from django.dispatch import receiver
from django.core.mail import mail_admins
from django.shortcuts import get_object_or_404

from my_homepage.contact_me.models import NewContact


@receiver(signals.post_save, sender=NewContact)
def notify_new_contact(sender, instance, created, **kwargs):
    '''Notifies admins of new contact form submission'''
    if created:
        contact = get_object_or_404(NewContact, id=instance.id)
        name = contact.name
        email = contact.email
        email_subject = contact.subject
        content =  contact.content
        subject = f'[New Contact Me] {email_subject}'
        message = content
        mail_admins(subject, message=message, fail_silently=False, connection=None, html_message=None)
