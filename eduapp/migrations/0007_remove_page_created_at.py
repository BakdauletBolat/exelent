# Generated by Django 3.2.2 on 2021-07-01 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0006_auto_20210519_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='created_at',
        ),
    ]
