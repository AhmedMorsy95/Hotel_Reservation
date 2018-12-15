# Generated by Django 2.0.5 on 2018-12-15 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('price', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0, unique=True)),
                ('room_type', models.CharField(choices=[(0, 'Single'), (1, 'Double'), (2, 'Triple')], max_length=1)),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel.hotel')),
            ],
        ),
    ]
