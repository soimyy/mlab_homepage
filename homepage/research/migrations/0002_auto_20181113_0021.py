# Generated by Django 2.0.7 on 2018-11-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='text',
            field=models.TextField(verbose_name='内容'),
        ),
    ]
