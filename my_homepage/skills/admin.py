from django.contrib import admin

from my_homepage.skills.models import SkillsOverview, Skill


@admin.register(SkillsOverview)
class SkillsOverviewAdmin(admin.ModelAdmin):
    list_display = ('overview',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'link', 'years_experience', 'notes',)
    list_filter = ('category', 'name',)
    list_display_links = ('name',)
    list_editable = ('link', 'years_experience', 'notes',)
    list_per_page = 50
    search_fields = ['name',]
