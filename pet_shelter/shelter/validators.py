import datetime

from django.core.exceptions import ValidationError


def validate_date_of_arrival(value):
    date_today = datetime.date.today()
    if value > date_today:
        raise ValidationError(f'Нельзя назначить дату прибытия животного будущим числом. Сегодня {date_today}')


def validate_positive(value):
    if value < 0:
        raise ValidationError(f'Возможно только положительное значение')
