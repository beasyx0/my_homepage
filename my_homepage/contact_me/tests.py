from django.test import TestCase
from django.core import mail
from django.shortcuts import reverse
from http import HTTPStatus
from my_homepage.contact_me.models import NewContact


data = {
    'name': 'Billy Bob',
    'email': 'someemail@email.com',
    'subject': 'This is a subject',
    'content': 'Lorem ipsum lorem ipsum',
}


class TestNewContact(TestCase):
    '''Tests new_contact models, routes and signals'''

    def setUp(self):

        new_contact = NewContact(
                        name=data['name'],
                        email=data['email'],
                        subject=data['subject'],
                        content=data['content'],
                    )
        new_contact.save()
        new_contact.refresh_from_db()


    def test_new_contact_post_url(self):
        '''Tests for successful form submission by looking for redirect'''

        print('Testing new contact post url')

        new_contact_url = reverse('new-contact')

        r = self.client.post(new_contact_url, data)

        # if redirect then success
        self.assertEqual(r.status_code, HTTPStatus.FOUND)

        print('Finished')

    def test_new_contact_post_url_get_not_allowed(self):
        '''Tests new contact route get now allowed'''

        print('Testing new contact post url get not allowed')

        new_contact_url = reverse('new-contact')
        r = self.client.get(new_contact_url)

        self.assertEqual(r.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

        print('Finished')


    def test_contact_me_save_and_str_method(self):
        '''Tests that a new about obj saves correctly'''
        
        print('Testing ContactMe save and str method')

        new_contact = NewContact.objects.first()

        self.assertEqual(data['name'], new_contact.__str__())
        self.assertEqual(data['name'], new_contact.name)
        self.assertEqual(data['email'], new_contact.email)
        self.assertEqual(data['subject'], new_contact.subject)
        self.assertEqual(data['content'], new_contact.content)

        print('Finished')

    def test_notify_of_new_contact_email_signal(self):
        '''Tests that a new email in outbox on NewContact save'''

        print('Testing new contact email signal')

        self.assertEqual(len(mail.outbox), 1)

        print('Finished')
