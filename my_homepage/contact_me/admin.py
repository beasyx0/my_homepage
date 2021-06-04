from django.contrib import admin

from my_homepage.contact_me.models import NewContact


@admin.register(NewContact)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'content',)
    search_fields = ['name', 'email',]
