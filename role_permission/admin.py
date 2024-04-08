from django.contrib import admin
from .models import RolePermission
# Register your models here.

class RolePermissionAdmin(admin.ModelAdmin):
        list_display = ["id","role_id","permission_id"]


admin.site.register(RolePermission,RolePermissionAdmin)