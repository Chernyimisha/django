# Generated by Django 5.0.3 on 2024-03-31 13:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dz2app', '0007_alter_customer_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='registration_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
