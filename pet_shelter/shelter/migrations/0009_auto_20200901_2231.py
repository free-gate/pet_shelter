# Generated by Django 3.1 on 2020-09-01 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0008_pet_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ['-date_of_arrival']},
        ),
    ]