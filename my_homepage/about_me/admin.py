from django.contrib import admin

from my_homepage.about_me.models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'github_link', 'location',)
    list_display_links = ('name',)
    search_fields = ['name', 'phone', 'email', 'github_link', 'location',]
