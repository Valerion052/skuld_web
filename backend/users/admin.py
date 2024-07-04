from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'role']
    list_filter = ['email', 'first_name']


admin.site.site_header = 'Administration'
admin.site.site_title = 'Administration'
admin.site.index_title = 'Administration'