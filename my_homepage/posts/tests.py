from django.test import TestCase
from django.shortcuts import reverse
from django.utils import timezone

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

    def test_tag_model_and_routes(self):
        '''Tests the tag model and routes'''

        print('Testing tag model and routes')

        tag = Tag.objects.first()

        tag_url = reverse('tag-detail', kwargs={'slug':tag.slug})

        r = self.client.get(tag_url)

        self.assertEqual(tag.name, 'Docker')
        self.assertEqual(r.status_code, 200)

        print('Finished')

    def test_post_model_routes_and_manager(self):
        '''Tests the post model and routes'''

        print('Testing post model and routes')

        post = Post.objects.first()

        search = Post.my_manager.search('content')
        search_vector = post.search_vector

        post_url = reverse('post-detail', kwargs={'slug':post.slug})

        r = self.client.get(post_url)

        now = timezone.now()

        self.assertTrue(search_vector is not None)
        self.assertEqual(len(search), 1)
        self.assertEqual(post.title, post.__str__())
        self.assertEqual(post.title, 'This is a title')
        self.assertEqual(post.content, 'This is some content')
        self.assertEqual(len(post.tags.all()), 1)
        self.assertEqual(post.date.date(), now.date())
        self.assertEqual(r.status_code, 200)

        print('Finished')
