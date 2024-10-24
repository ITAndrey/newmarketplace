from django.core.exceptions import ValidationError
import re


def validate_password(value):
    if not (
        len(value) >= 10 and
        re.search(r'[A-Z]', value) and
        re.search(r'[a-z]', value) and
        re.search(r'[~!@#$%^&*]', value) and
        re.search(r'\d', value)
    ):
        raise ValidationError("Пароль не соответствует требованиям.")