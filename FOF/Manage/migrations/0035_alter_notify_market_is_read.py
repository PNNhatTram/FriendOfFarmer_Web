# Generated by Django 5.0.2 on 2024-05-05 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manage', '0034_notify_market'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify_market',
            name='is_read',
            field=models.BooleanField(default=0),
        ),
    ]
