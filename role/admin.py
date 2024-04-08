from django.contrib import admin
from .models import Role

class RoleAdmin(admin.ModelAdmin):
    list_display = ["role_id", "role_name"]


admin.site.register(Role,RoleAdmin)