from django.apps import AppConfig


class ContactMeConfig(AppConfig):
    name = 'my_homepage.contact_me'

    def ready(self):
        import my_homepage.contact_me.signals
