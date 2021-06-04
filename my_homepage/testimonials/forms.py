from django.conf import settings
from django import forms

from my_homepage.testimonials.models import Testimonial


class TestimonialForm(forms.ModelForm):
    '''Form for testimonial submissions on homepage'''
    class Meta:
        model = Testimonial
        fields = ('name', 'comment',)
