# Generated by Django 5.0.3 on 2024-03-30 17:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksapp', '0004_alter_throws_time_throws'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('biography', models.TextField(max_length=1000)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='throws',
            name='time_throws',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]