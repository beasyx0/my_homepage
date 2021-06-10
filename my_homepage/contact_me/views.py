from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from my_homepage.contact_me.models import NewContact
from my_homepage.contact_me.forms import NewContactForm
from my_homepage.utils.my_utils import process_recaptcha


@require_POST
def new_contact(request):
    '''View to process contact form submission on homepage'''
    new_contact_form = NewContactForm(request.POST or None)
    if new_contact_form.is_valid():
        passed_recaptcha = process_recaptcha(request)
        name = new_contact_form.instance.name
        if passed_recaptcha:
            new_contact_form.save()
            messages.success(request, f'Thank you {name}, I will reply shortly.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('home')
    else:
        messages.error(request, 'Something went wrong, check the form')
        return redirect('home')
