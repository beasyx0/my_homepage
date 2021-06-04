from django.contrib import admin

from my_homepage.posts.models import Tag, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('date', 'title', 'slug',)
    list_filter = ('tags',)
    list_display_links = ('date',)
    list_editable = ('title',)
    list_per_page = 50
    list_select_related = True
    search_fields = ['title', 'content',]
    fieldsets = (
            (None, {
                'fields': ('date', 'title', 'slug', 'content', 'tags',),
            }),
        )
    filter_horizontal = ['tags']
    autocomplete_fields = ['tags']
    readonly_fields = ('date', 'slug',)
    filter_horizontal = ['tags']

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        qs = qs.defer('content',).prefetch_related('tags')
        return qs


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ['title', 'content',]
