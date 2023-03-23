import datetime

from django.core.exceptions import ValidationError


def validate_birth_date(value):
    if value >= (datetime.datetime.now() + datetime.timedelta(days=1)).date():
        raise ValidationError("%(value) cannot be later than today", params={'value': value})
