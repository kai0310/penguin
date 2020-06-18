# Generated by Django 3.0.7 on 2020-06-18 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='status',
            field=models.CharField(choices=[('waiting', '待機中'), ('calling', '呼出中'), ('handling', '対応中'), ('accepted', '登録完了'), ('invalid', '無効')], default='waiting', max_length=10, verbose_name='状態'),
        ),
    ]