# Generated by Django 3.0.7 on 2020-06-18 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20200618_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='accept_id',
            new_name='submit_id',
        ),
    ]
