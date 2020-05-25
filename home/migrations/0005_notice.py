# Generated by Django 3.0.6 on 2020-05-25 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_usertoken_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('body', models.TextField(max_length=100, verbose_name='本文')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='最終更新日時')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='入力者')),
            ],
            options={
                'verbose_name': 'お知らせ',
                'verbose_name_plural': 'お知らせ',
            },
        ),
    ]
