# Generated by Django 2.1.4 on 2018-12-25 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0002_extend_stay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extend_stay',
            name='confirmed',
        ),
        migrations.RemoveField(
            model_name='extend_stay',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='extend_stay',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='extend_stay',
            name='room_id',
        ),
        migrations.AddField(
            model_name='extend_stay',
            name='reservation_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Reservation.Reservations'),
        ),
    ]
