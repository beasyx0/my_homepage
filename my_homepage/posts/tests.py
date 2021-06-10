from django.test import TestCase
from django.shortcuts import reverse
from django.utils import timezone
from http import HTTPStatus
from my_homepage.posts.models import _get_unique_slug, Tag, Post


class TestPosts(TestCase):
    '''Tests the post models and routes'''

    def setUp(self):
        tag = Tag.objects.create(name='Docker')
        post = Post.objects.create(
                    title='This is a title',
                    content='This is some content',
                    
                )
        new_tags = Tag.objects.all()
        post.tags.set(new_tags)
        post.save()

    def test_tag_model_and_str_method(self):
        '''Tests the tag model and routes'''

        print('Testing tag model and str method')

        tag = Tag.objects.first()

        self.assertEqual(tag.name, 'Docker')
        self.assertEqual(tag.__str__(), 'Docker')

        print('Finished')

    def test_tag_route_get(self):
        '''Tests for a 200 response on tag-detail page'''

        print('Testing tag route and get')

        tag = Tag.objects.first()

        tag_url = reverse('tag-detail', kwargs={'slug':tag.slug})

        r = self.client.get(tag_url)

        self.assertEqual(r.status_code, HTTPStatus.OK)

        print('Finished')

    def test_tag_route_post_not_allowed(self):
        '''Tests tag route post not allowed'''

        print('Testing tag route post not allowed')

        tag = Tag.objects.first()

        tag_url = reverse('tag-detail', kwargs={'slug': tag.slug})

        r = self.client.post(tag_url)

        self.assertEqual(r.status_code, HTTPStatus.METHOD_NOT_ALLOWED)


    def test_post_model_and_manager(self):
        '''Tests the post model and routes'''

        print('Testing post model and manager')

        post = Post.objects.first()

        search = Post.my_manager.search('content')
        search_vector = post.search_vector

        now = timezone.now()

        self.assertTrue(search_vector is not None)
        self.assertEqual(len(search), 1)
        self.assertEqual(post.title, post.__str__())
        self.assertEqual(post.title, 'This is a title')
        self.assertEqual(post.content, 'This is some content')
        self.assertEqual(len(post.tags.all()), 1)
        self.assertEqual(post.date.date(), now.date())

        print('Finished')

    def test_post_route_get(self):
        '''Tests for a 200 response on the post-detail page'''

        print('Testing post route')

        post = Post.objects.first()

        post_url = reverse('post-detail', kwargs={'slug': post.slug})

        r = self.client.get(post_url)

        self.assertEqual(r.status_code, HTTPStatus.OK)

        print('Finished')

    def test_post_route_post_not_allowed(self):
        '''Test post route post not allowed'''

        print('Testing post route post not allowed')

        post = Post.objects.first()

        post_url = reverse('post-detail', kwargs={'slug': post.slug})

        r = self.client.post(post_url)

        self.assertEqual(r.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

        print('Finished')
