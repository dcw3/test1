# Generated by Django 2.0.3 on 2018-03-24 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=-1)),
                ('vehicle_miles', models.IntegerField(default=0)),
            ],
        ),
    ]
