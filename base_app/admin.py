from django.contrib import admin

# Register your models here.
# base_app/admin.py

from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'phone', 'birthday', 'location')
    search_fields = ('name', 'email', 'phone', 'location')
    list_filter = ('location', 'birthday')

admin.site.register(Profile, ProfileAdmin)
