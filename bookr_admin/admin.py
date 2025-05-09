from django.contrib import admin

# Register your models here.
class BookrAdmin(admin.AdminSite):
    site_header = "Bookr Administration Portal"
    site_title = "Bookr Administration Portal"
    index_title = "Bookr Administration"
