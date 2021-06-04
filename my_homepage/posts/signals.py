from django.db.models import signals
from django.dispatch import receiver
from django.db import transaction
from django.contrib.postgres.search import SearchVector

from my_homepage.posts.models import Post


@receiver(signals.post_save, sender=Post)
def update_search_vectors(sender, instance, created, **kwargs):
    '''Updates postgres search vectors on save'''
    search_vectors = SearchVector('title', weight='A') + SearchVector('content', weight='B')
    if created:
        instance.search_vector = search_vectors
        instance.save()
