from django.test import TestCase
from django.shortcuts import reverse
from http import HTTPStatus

# TODO: add test for post method error
class TestHomePage(TestCase):
    '''Tests for homepage app and robots txt'''

    def test_homepage_route_get(self):
        '''Tests that we get a 200 response on homepage'''

        print('Testing homepage route')

        homepage_url = reverse('home')
        r = self.client.get(homepage_url)

        self.assertEqual(r.status_code, HTTPStatus.OK)

        print('Finished')

    def test_homepage_route_post_not_allowed(self):
        '''Tests that post method is denied'''

        print('Testing homepage route post not allowed')

        homepage_url = reverse('home')
        r = self.client.post(homepage_url)

        self.assertEqual(r.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

        print('Finished')

    def test_robots_txt_get(self):
        '''Tests the robots txt is loaded properly'''

        print('Testing robots txt get')

        robots_url = reverse('robots-txt')
        r = self.client.get(robots_url)

        lines = r.content.decode().splitlines()
        self.assertEqual(lines[0], "User-Agent: *")

        self.assertEqual(r["content-type"], "text/plain")
        
        
        self.assertEqual(r.status_code, HTTPStatus.OK)

        print('Finished')

    def test_robots_txt_post_not_allowed(self):
        '''Tests that post method is denied'''

        print('Testing robots txt post not allowed')

        robots_url = reverse('robots-txt')
        r = self.client.post(robots_url)

        self.assertEqual(HTTPStatus.METHOD_NOT_ALLOWED, r.status_code)

        print('Finished')
