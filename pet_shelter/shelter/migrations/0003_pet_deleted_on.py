# Generated by Django 3.1 on 2020-08-29 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0002_auto_20200829_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='deleted_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]