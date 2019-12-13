from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ApplicationsConfig(AppConfig):
    name = "rest_example.applications"
    verbose_name = _("Applications")

    def ready(self):
        try:
            import rest_example.applications.signals  # noqa F401
        except ImportError:
            pass
