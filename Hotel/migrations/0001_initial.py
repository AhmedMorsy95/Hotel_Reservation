# Generated by Django 2.1.3 on 2018-12-11 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Location', '0001_initial'),
        ('Owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.FloatField(blank=True, default=None, null=True)),
                ('stars', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='media')),
                ('rates_count', models.IntegerField(default=0)),
                ('rates_sum', models.IntegerField(default=0)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Location.location')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Owner.owner')),
            ],
        ),
    ]
