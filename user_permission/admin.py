from django.contrib import admin
from .models import UserPermission
# Register your models here.

class UserPermissionAdmin(admin.ModelAdmin):
        list_display = ["id","user_id","permission_id"]

admin.site.register(UserPermission,UserPermissionAdmin)
