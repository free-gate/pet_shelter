# Generated by Django 3.1 on 2020-09-01 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0010_auto_20200901_2232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ['-date_of_arrival']},
        ),
    ]