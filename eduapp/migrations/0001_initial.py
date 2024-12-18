# Generated by Django 3.2.2 on 2021-05-19 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('subTitle', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='SlideImages/')),
                ('linkTo', models.CharField(max_length=255)),
            ],
        ),
    ]
