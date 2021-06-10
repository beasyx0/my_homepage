from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET

from my_homepage.about_me.models import About


@require_GET
def about(request):
    '''About me page'''
    title = 'About Me'
    context = {
        'title': title,
    }
    return TemplateResponse(request, 'pages/about.html', context)
