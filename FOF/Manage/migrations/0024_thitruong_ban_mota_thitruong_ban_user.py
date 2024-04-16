# Generated by Django 5.0.3 on 2024-04-16 14:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manage', '0023_customer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='thitruong_ban',
            name='mota',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AddField(
            model_name='thitruong_ban',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
