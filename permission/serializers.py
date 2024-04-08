from rest_framework import serializers

from permission.models import Permission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ["permission_id", "permission_name", "permission_description"]
