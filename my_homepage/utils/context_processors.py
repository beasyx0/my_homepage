from django.conf import settings
from django.contrib.sites.models import Site
from my_homepage.about_me.models import About
from my_homepage.skills.models import SkillsOverview, Skill
from my_homepage.posts.models import Post
from my_homepage.testimonials.models import Testimonial
from my_homepage.testimonials.forms import TestimonialForm
from my_homepage.contact_me.forms import NewContactForm


def settings_context(_request):
    return {"DEBUG": settings.DEBUG}


def extra_context(request):
    '''Context available sitewide'''
    return {
        'my_site': Site.objects.last(),
        'canonical_path': request.build_absolute_uri(request.path),
        'about': About.objects.last(),
        'skills_overview': SkillsOverview.objects.last(),
        'all_skills': Skill.objects.values(),
        'latest_posts': Post.objects.prefetch_related('tags').order_by('-date')[:5],
        'testimonials': Testimonial.objects.order_by('-id').filter(approved=True)[:3],
        'testimonial_form': TestimonialForm(request.POST or None),
        'new_contact_form': NewContactForm(request.POST or None),
        }
