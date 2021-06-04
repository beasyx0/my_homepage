import uuid
from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.shortcuts import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify

from tinymce import HTMLField

from my_homepage.posts.managers import PostManager


def _get_unique_slug(string_to_slug: str):
    '''Takes in a str and gives back a slug with uuid'''
    slug = slugify(string_to_slug)
    num = str(uuid.uuid4().hex)
    unique_slug = f'{slug}-{num}'
    qs_exists = Post.objects.filter(slug=unique_slug)
    if qs_exists:
        _get_unique_slug(self)
    return unique_slug


class Tag(models.Model):
    '''Tag model for posts'''
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(editable=False, max_length=255, unique=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={
            'slug': self.slug
        })

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = timezone.now()
            self.slug = _get_unique_slug(self.name)
        return super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
    '''Simple post model with full text editor (tinymce4)'''
    date = models.DateTimeField(editable=False)
    slug = models.SlugField(editable=False, max_length=255, unique=True, null=True)
    title = models.CharField(max_length=200, unique=True)
    content = HTMLField()
    tags = models.ManyToManyField(Tag, related_name='posts')
    search_vector = SearchVectorField(null=True)

    objects = models.Manager()
    my_manager = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'slug': self.slug
        })

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = timezone.now()
            self.slug = _get_unique_slug(self.title)
        return super(Post, self).save(*args, **kwargs)
