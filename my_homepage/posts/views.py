from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET, require_POST
from django.contrib import messages

from my_homepage.about_me.models import About
from my_homepage.posts.models import Tag, Post


@require_GET
def search(request):
    '''Postgres full-text search. Uses model manager my_manager.search'''
    title = 'Search results'
    search_term = request.GET.get('q', None)
    punctuation = '''!()-[]|{};:'"\,<>./?@#$%^&*_~''' # punctuation to check against
    clean_search_term = ''

    if not search_term:
        messages.error(request, 'Please enter a search term')
        return redirect('home')

    for i in search_term:
        if i not in punctuation:
            clean_search_term += i

    posts = Post.my_manager.search(clean_search_term)

    if not posts:
        messages.error(request, f'Nothing found with the search term {clean_search_term}')
        return redirect('home')

    context = {
        'title': title,
        'search_term': clean_search_term,
        'posts': posts,
    }
    return TemplateResponse(request, 'pages/search.html', context)


@require_GET
def post_detail(request, slug):
    '''Post detail view'''
    title = 'Post Detail'
    post = get_object_or_404(Post, slug=slug)
    context = {
        'title': title,
        'post': post,
    }
    return TemplateResponse(request, 'pages/post-detail.html', context)


@require_GET
def tag_detail(request, slug):
    '''Tag detail view'''
    title = 'Tag Detail'
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag).prefetch_related('tags').order_by('-date')
    context = {
        'title': title,
        'tag': tag,
        'posts': posts,
    }
    return TemplateResponse(request, 'pages/tag-detail.html', context)
