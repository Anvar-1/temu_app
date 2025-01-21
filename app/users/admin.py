from django.contrib import admin
from .models import User

admin.site.register(User)
class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']