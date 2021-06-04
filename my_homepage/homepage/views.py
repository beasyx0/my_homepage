from django.core.cache import cache
from django.template.response import TemplateResponse
from django.http import HttpResponseForbidden

from my_homepage.about_me.models import About
from my_homepage.skills.models import SkillsOverview, Skill
from my_homepage.posts.models import Post, Tag
from my_homepage.testimonials.models import Testimonial
from my_homepage.testimonials.forms import TestimonialForm


def home(request):
    '''Homepage view'''
    if request.method == 'GET':

        title = 'Home'
        context = {
            'title': title,
        }
        return TemplateResponse(request, 'pages/home.html', context)
    else:
        HttpResponseForbidden('You can not do that')