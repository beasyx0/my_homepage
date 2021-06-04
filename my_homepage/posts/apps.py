from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'my_homepage.posts'

    def ready(self):
        import my_homepage.posts.signals
