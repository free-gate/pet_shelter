# Generated by Django 3.1 on 2020-08-29 19:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0004_auto_20200829_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='date_of_arrival',
            field=models.DateField(default=datetime.datetime(2020, 8, 29, 19, 39, 53, 915066, tzinfo=utc)),
        ),
    ]
