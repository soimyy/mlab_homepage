# Generated by Django 2.0.7 on 2018-11-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20181015_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='写真'),
        ),
    ]
