from django.contrib import admin

from my_homepage.testimonials.models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('date', 'name', 'approved',)
    list_filter = ('approved',)
    search_fields = ['name',]
    fieldsets = (
            (None, {
                'fields': ('date', 'name', 'comment', 'approved',),
            }),
        )
    readonly_fields = ('date',)
    actions = ['mark_testimonials_approved',]


    def mark_testimonials_approved(self, request, queryset):
        for obj in queryset:
            if not obj.approved:
                obj.approved = True
                obj.save()
            else:
                obj.approved = False
                obj.save()

        self.message_user(request, 'Testimonials marked approved or not approved')
