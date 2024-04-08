from django.contrib import admin
from authentication_module.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
    # list_display = ["id", "email", "name", "phone",
    #                 "date_of_birth", "gender", "address", "password", "is_verified", "is_admin", "is_superuser"]
    list_display = ["id", "email", "name", "phone",
                    "date_of_birth", "gender", "address", "role_id", "password", "is_verified", "is_admin", "is_superuser"]
    list_filter = ["is_admin", "is_superuser", "is_verified"]
    fieldsets = [
        ('User Credentials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": [
         "name", "phone", "date_of_birth", "gender", "address", "role_id"]}),
        ("Permissions", {"fields": [
         "is_admin", "is_superuser", "is_verified"]}),
    ]
    # fieldsets = [
    #     ('User Credentials', {"fields": ["email", "password"]}),
    #     ("Personal info", {"fields": [
    #      "name", "phone", "date_of_birth", "gender", "address"]}),
    #     ("Permissions", {"fields": [
    #      "is_admin", "is_superuser", "is_verified"]}),
    # ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "phone", "date_of_birth", "gender", "address", "role_id", "password1", "password2"],
            },
        ),
    ]
    # add_fieldsets = [
    #     (
    #         None,
    #         {
    #             "classes": ["wide"],
    #             "fields": ["email", "name", "phone", "date_of_birth", "gender", "address", "password1", "password2"],
    #         },
    #     ),
    # ]
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []


admin.site.register(User, UserModelAdmin)
