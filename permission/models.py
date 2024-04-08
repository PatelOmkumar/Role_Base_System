from django.db import models

# Create your models here.


class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True)
    permission_name = models.CharField(max_length=255, unique=True)
    permission_description = models.CharField(max_length=200)

