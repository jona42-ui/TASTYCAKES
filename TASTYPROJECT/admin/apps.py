from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # default_site = 'django.contrib.admin.sites.AdminSite'
    name = 'admin'
