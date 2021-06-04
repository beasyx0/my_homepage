from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.template.response import TemplateResponse

from my_homepage.about_me.models import About


def about(request):
    '''About me page'''
    if request.method == 'GET':
        title = 'About Me'
        context = {
            'title': title,
        }
        return TemplateResponse(request, 'pages/about.html', context)
    else:
        HttpResponseForbidden('You can not do that')
