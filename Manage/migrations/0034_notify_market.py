# Generated by Django 5.0.2 on 2024-05-05 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manage', '0033_adress_alter_plant_plant_nd_alter_product_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='notify_market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timejoin', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField()),
                ('customer', models.ManyToManyField(related_name='customer', to='Manage.customer')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maker', to='Manage.market')),
                ('makerAuth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='makerAuth', to='Manage.customer')),
            ],
        ),
    ]
