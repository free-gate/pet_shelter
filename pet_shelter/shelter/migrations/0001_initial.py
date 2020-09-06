# Generated by Django 3.1 on 2020-09-06 20:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shelter.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField()),
                ('date_of_arrival', models.DateField(default=datetime.date.today, validators=[shelter.validators.validate_date_of_arrival])),
                ('weight_kg', models.FloatField(validators=[shelter.validators.validate_positive])),
                ('height_cm', models.FloatField(validators=[shelter.validators.validate_positive])),
                ('special_sign', models.TextField()),
                ('deleted_on', models.DateField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_of_arrival'],
            },
        ),
    ]
