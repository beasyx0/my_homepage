from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

from my_homepage.homepage.views import home
from my_homepage.about_me.views import about
from my_homepage.posts.views import search, post_detail, tag_detail
from my_homepage.testimonials.views import new_testimonial
from my_homepage.contact_me.views import new_contact


# admin header, etc.
admin.site.site_title = "My Homepage Admin"
admin.site.site_header = "My Homepage Admin"
admin.site.index_title = ""
admin.site.enable_nav_sidebar = False


urlpatterns = [
    path("", home, name="home"),
    path("search/", search, name='search'),
    path("post-detail/<slug>/", post_detail, name="post-detail",),
    path("tag-detail/<slug>/", tag_detail, name="tag-detail",),
    path("about/", about, name="about",),
    path("new-testimonial/", new_testimonial, name="new-testimonial"),
    path("new-contact/", new_contact, name="new-contact"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("tinymce/", include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
