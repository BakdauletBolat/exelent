# Generated by Django 3.1.7 on 2021-03-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_auto_20210326_2230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mail',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AddField(
            model_name='mail',
            name='consent',
            field=models.BooleanField(blank=True, null=True, verbose_name='Согласие'),
        ),
        migrations.AddField(
            model_name='mail',
            name='lastname',
            field=models.CharField(default=1, max_length=255, verbose_name='Отчество'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mail',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='mail',
            name='surname',
            field=models.CharField(default=1, max_length=255, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mail',
            name='universityjob',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Вуз'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='phone',
            field=models.CharField(max_length=255, verbose_name='Контактный телефон:'),
        ),
    ]
