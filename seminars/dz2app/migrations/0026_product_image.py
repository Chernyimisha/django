# Generated by Django 5.0.3 on 2024-04-04 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dz2app', '0025_alter_order_date_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
