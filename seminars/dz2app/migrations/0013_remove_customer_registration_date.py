# Generated by Django 5.0.3 on 2024-03-31 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dz2app', '0012_alter_customer_registration_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='registration_date',
        ),
    ]
