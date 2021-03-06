# Generated by Django 3.0.6 on 2020-05-26 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200526_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='表題')),
                ('body', models.TextField(max_length=2000, verbose_name='本文')),
                ('read', models.BooleanField(default=False, verbose_name='既読')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='送信日時')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_from', to=settings.AUTH_USER_MODEL, verbose_name='送信者')),
                ('to', models.ManyToManyField(related_name='notification_to', to=settings.AUTH_USER_MODEL, verbose_name='宛先')),
            ],
            options={
                'verbose_name': '通知',
                'verbose_name_plural': '通知',
            },
        ),
    ]
