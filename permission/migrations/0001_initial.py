# Generated by Django 5.0.2 on 2024-04-08 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('permission_id', models.AutoField(primary_key=True, serialize=False)),
                ('permission_name', models.CharField(max_length=255, unique=True)),
                ('permission_description', models.CharField(max_length=200)),
            ],
        ),
    ]
