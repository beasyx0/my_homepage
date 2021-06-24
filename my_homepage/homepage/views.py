from django.core.cache import cache
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.views.decorators.http import require_GET

from my_homepage.about_me.models import About
from my_homepage.skills.models import SkillsOverview, Skill
from my_homepage.posts.models import Post, Tag
from my_homepage.testimonials.models import Testimonial
from my_homepage.testimonials.forms import TestimonialForm


@require_GET
def home(request):
    '''Homepage view. All context is stored in utils/context_processors'''
    title = 'Home'
    context = {
        'title': title,
    }
    return TemplateResponse(request, 'pages/home.html', context)


@require_GET
def robots_txt(request):
    '''robots.txt view'''
    lines = [
        "User-Agent: *",
        "Disallow: /",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
