# Generated by Django 3.0.7 on 2020-06-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_engeki_ground_mogiten_okunai_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='accept_id',
            field=models.SlugField(max_length=5, null=True, verbose_name='申請コード'),
        ),
    ]
