from django.apps import AppConfig


class BookrAdminConfig(AppConfig):
    default_site = 'bookr_admin.admin.BookrAdmin'
    name = 'bookr_admin'
