from django.db import models
from django.core.validators import RegexValidator


class Phones_n_codes(models.Model):
    phone = models.CharField(
        'phone',
        validators=[RegexValidator(regex='^8[0-9]{10}$', message='Incorrect phone')],
    )
    self_code = models.CharField(max_length=6)
    entered_code = models.CharField(
        'entered_code',
        validators=[RegexValidator(regex='^[0-9a-zA-Z]{6}$', message='Incorrect code')],
    )