from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "platform_control.users"
    verbose_name = _("Usuarios")

    def ready(self):
        try:
            import platform_control.users.signals  # noqa F401
        except ImportError:
            pass
