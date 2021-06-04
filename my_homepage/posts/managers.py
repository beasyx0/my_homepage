from django.contrib.postgres.aggregates import StringAgg
from django.contrib.postgres.search import (
    SearchQuery, SearchRank, SearchVector, TrigramSimilarity,
)
from django.db import models


class PostManager(models.Manager):
    '''Post manager. Holds methods to work with Post model at the table level'''
    def search(self, search_text):
        '''Postgres full-text search with rank and trigram similarity'''

        search_vectors = (
            SearchVector('title', weight='A', config='english') +
            SearchVector(StringAgg('content', delimiter=' '), weight='B', config='english',)
        )

        search_query = SearchQuery(
            search_text, config='english'
        )

        search_rank = SearchRank(search_vectors, search_query)
        trigram_similarity = TrigramSimilarity('title', search_text)

        return self.filter(
            search_vector=search_query)\
            .prefetch_related('tags')\
            .annotate(rank=search_rank + trigram_similarity)\
            .order_by('-rank')