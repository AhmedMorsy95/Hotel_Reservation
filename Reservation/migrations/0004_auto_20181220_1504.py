# Generated by Django 2.1.4 on 2018-12-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0003_remove_reservations_hotel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='from_date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='to_date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
