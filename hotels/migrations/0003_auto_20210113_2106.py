# Generated by Django 3.1.5 on 2021-01-13 19:06

from django.db import migrations, models
import hotels.models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_booking_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='origin',
            field=hotels.models.PatchedPlaceField(blank=True, max_length=255),
        ),
    ]
