import json
import urllib

from django.conf import settings
from django.views.decorators.http import require_POST
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages

from my_homepage.testimonials.forms import TestimonialForm
from my_homepage.utils.my_utils import process_recaptcha


@require_POST
def new_testimonial(request):
    '''Submits new testimonial on the homepage'''
    testimonial_form = TestimonialForm(request.POST or None)
    if testimonial_form.is_valid():
        recaptcha_passed = process_recaptcha(request)

        if recaptcha_passed:
            testimonial_form.save()
            name = testimonial_form.instance.name
            messages.success(request, f'Thanks {name}! Your testimonial has been recieved.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('home')
