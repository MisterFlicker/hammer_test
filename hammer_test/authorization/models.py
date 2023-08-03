from django.db import models
from django.core.validators import RegexValidator


class Phones_n_codes(models.Model):
    phone = models.CharField(
        'phone',
        max_length=11,
    )
    self_code = models.CharField(max_length=6)
    entered_code = models.CharField(
        'entered_code',
        max_length=6,
    )