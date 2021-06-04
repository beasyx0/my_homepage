from django.apps import AppConfig


class TestimonialsConfig(AppConfig):
    name = 'my_homepage.testimonials'

    def ready(self):
        import my_homepage.testimonials.signals
