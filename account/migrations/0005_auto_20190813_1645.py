# Generated by Django 2.1.7 on 2019-08-13 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190813_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uservisited',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='uservisited',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserVisited',
        ),
    ]
