# Generated by Django 3.0.6 on 2020-05-31 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20200529_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupinfo',
            name='slack_ch',
            field=models.CharField(max_length=100, verbose_name='slack channel'),
        ),
    ]
