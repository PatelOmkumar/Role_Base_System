from rest_framework import serializers

from user_permission.models import UserPermission


class UserPermissionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = UserPermission
        fields = ["id", "user_id", "permission_id"]
