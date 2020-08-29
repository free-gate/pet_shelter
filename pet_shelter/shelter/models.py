import datetime

from django.db import models

from . import validators


class Pet(models.Model):
    nickname = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    date_of_arrival = models.DateField(default=datetime.date.today, validators=[validators.validate_date_of_arrival])
    weight_kg = models.FloatField(validators=[validators.validate_positive])
    height_cm = models.FloatField(validators=[validators.validate_positive])
    special_sign = models.TextField()
    deleted_on = models.DateField(null=True,  blank=True)

    def __str__(self):
        return f"{self.nickname} {self.date_of_arrival}"
