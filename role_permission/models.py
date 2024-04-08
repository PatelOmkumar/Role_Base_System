from django.db import models

from permission.models import Permission
from role.models import Role

# Create your models here.

class RolePermission(models.Model):
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission_id = models.ForeignKey(Permission, on_delete=models.CASCADE)
