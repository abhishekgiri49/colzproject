# Generated by Django 2.1.7 on 2019-08-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20190816_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='latitude',
            field=models.FloatField(blank=True, default='27.6817'),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='longitude',
            field=models.FloatField(blank=True, default='85.3170'),
        ),
    ]
