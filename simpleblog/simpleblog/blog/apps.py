from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogConfig(AppConfig):
    name = "simpleblog.blog"
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = _("Blogs")

    def ready(self):
        try:
            import simpleblog.users.signals  # noqa F401
        except ImportError:
            pass

