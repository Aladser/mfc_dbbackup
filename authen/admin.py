from django.contrib import admin
from authen.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'last_name', 'patronym', 'worker_position', 'is_active')
    ordering = ('pk',)

