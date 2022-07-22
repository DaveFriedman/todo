from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppCoreConfig(AppConfig):
    name = 'todo.appcore'
    verbose_name = _("Todo")
