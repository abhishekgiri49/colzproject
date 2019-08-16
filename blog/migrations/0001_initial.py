# Generated by Django 2.2.1 on 2019-05-03 07:28

import ckeditor_uploader.fields
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='img')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('temperature', models.FloatField(default='1')),
                ('difficulty', models.FloatField(default='1')),
                ('security', models.FloatField(default='1')),
                ('trekking_type', multiselectfield.db.fields.MultiSelectField(choices=[('Cycling', 'Cycling'), ('Walking', 'Walking'), ('Biking', 'Biking'), ('Peak Climbing', 'Peak Climbing'), ('Others', 'Others')], default='Walking', max_length=43)),
                ('destinaton_type', multiselectfield.db.fields.MultiSelectField(choices=[('Adventure', 'Adventure'), ('Pilgrims', 'Pilgrims'), ('Waterbody', 'Waterbody'), ('Himalayas', 'Himalayas'), ('Nature Seeing', 'Nature Seeing'), ('Others', 'Others')], default='Adventure', max_length=59)),
                ('accomodation_type', multiselectfield.db.fields.MultiSelectField(choices=[('Hotel', 'Hotel'), ('Teahouse', 'Teahouse'), ('Motel', 'Motel'), ('Tent', 'Tent'), ('Homestay', 'Homestay')], default='Hotel', max_length=34)),
                ('latitude', models.FloatField(default='1')),
                ('longitude', models.FloatField(default='1')),
                ('action', models.CharField(choices=[('publish', 'Publish'), ('draft', 'Draft')], default='draft', max_length=50)),
            ],
        ),
    ]