from django.test import TestCase
from django.core import mail
from django.shortcuts import reverse
from django.utils import timezone
from http import HTTPStatus
from my_homepage.testimonials.models import Testimonial


data = {
    'name': 'Billy Bob',
    'comment': 'This guy is the man',
}


class TestTestimonials(TestCase):
    '''Tests Testimonials models, routes and signals'''

    def setUp(self):
        Testimonial.objects.create(
                name=data['name'],
                comment=data['comment'],
            )

    def test_new_testimonial_route_post(self):
        '''Tests for successful form submission by looking for redirect'''

        print('Testing new testimonial post url')

        new_testimonial_url = reverse('new-testimonial')

        r = self.client.post(new_testimonial_url, data)

        # if redirect then success
        self.assertEqual(r.status_code, HTTPStatus.FOUND)

        print('Finished')

    def test_new_testimonial_route_get_not_allowed(self):
        '''Tests new testimonial route get not allowed'''

        print('Testing new testimonial route get not allowed')

        new_testimonial_url = reverse('new-testimonial')

        r = self.client.get(new_testimonial_url)

        # if redirect then success
        self.assertEqual(r.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

        print('Finished')

    def test_testinonial_save_and_str_method(self):
        '''Tests that a new Testimonial obj saves correctly'''

        testimonial = Testimonial.objects.first()

        now = timezone.now()

        self.assertEqual(testimonial.__str__(), data['name'])
        self.assertEqual(testimonial.date.date(), now.date())
        self.assertEqual(testimonial.name, data['name'])
        self.assertEqual(testimonial.comment, data['comment'])
        self.assertFalse(testimonial.approved)

    def test_notify_of_new_testimonial_email_signal(self):
        '''Tests that a new email in outbox on Testimonial save'''

        print('Testing new testimonial email signal')

        self.assertEqual(len(mail.outbox), 1)

        print('Finished')
