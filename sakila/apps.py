from __future__ import unicode_literals
from django.apps import AppConfig

# django signals 설정
class SakilaConfig(AppConfig):
    name = "sakila"
    verbose_name = 'Sakila Erp Test'

    def ready(self):
        from . import signals   # noqa