# Generated by Django 4.2.4 on 2023-08-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisement', '0003_advertisement_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default=' ', upload_to='advertisements/', verbose_name='Изображения'),
            preserve_default=False,
        ),
    ]
