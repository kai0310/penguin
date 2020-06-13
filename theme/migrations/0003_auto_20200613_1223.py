# Generated by Django 3.0.7 on 2020-06-13 12:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_auto_20200613_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='description',
            field=models.TextField(max_length=400, validators=[django.core.validators.MinLengthValidator(100)], verbose_name='趣意文'),
        ),
    ]
