from django.test import TestCase
from django.utils import timezone
from django.shortcuts import reverse

from my_homepage.about_me.models import About


class TestAbout(TestCase):
    '''Tests about models and url routes'''


    def test_about_detail_url(self):
        '''Tests for 200 response for about details page'''

        print('Testing about detail url')

        about_url = reverse('about')
        r = self.client.get(about_url)

        self.assertEqual(r.status_code, 200)

        print('Finished')


    def test_about_save_and_str_method(self):
        '''Tests that a new about obj saves correctly'''
        
        print('Testing about save and str method')

        data = {
            'name': 'Billy Bob',
            'phone': '2220002222',
            'email': 'someemail@email.com',
            'github_link': 'https://www.github.com/someguy/',
            'location': 'Mars',
            'about': 'lorem ipsum',
        }

        about = About(
            name=data['name'],
            phone=data['phone'],
            email=data['email'],
            github_link=data['github_link'],
            location=data['location'],
            about=data['about'],
                )
        about.save()
        about.refresh_from_db()

        self.assertEqual(data['name'], about.__str__())
        self.assertEqual(data['name'], about.name)
        self.assertEqual(data['phone'], about.phone)
        self.assertEqual(data['email'], about.email)
        self.assertEqual(data['github_link'], about.github_link)
        self.assertEqual(data['location'], about.location)
        self.assertEqual(data['about'], about.about)

        print('Finished')
