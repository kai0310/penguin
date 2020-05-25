# Generated by Django 3.0.6 on 2020-05-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200525_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='body',
            field=models.TextField(help_text='100 文字以内で入力してください。あまり長い文章は好ましくありません。', max_length=100, verbose_name='本文'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(help_text='15 文字以内で入力してください。', max_length=15, verbose_name='タイトル'),
        ),
    ]