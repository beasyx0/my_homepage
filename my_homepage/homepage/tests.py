from django.test import TestCase
from django.shortcuts import reverse


class TestHomePage(TestCase):
    '''Tests for homepage app'''

    def test_homepage_route(self):
        '''Tests that we get a 200 response on homepage'''

        print('Testing homepage route')

        homepage_url = reverse('home')
        r = self.client.get(homepage_url)

        self.assertEqual(r.status_code, 200)

        print('Finished')
