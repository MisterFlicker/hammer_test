from django.forms import ModelForm
from django.db import models
from django.core.validators import RegexValidator


class ThePhone(models.Model):
    phone = models.CharField('phone', validators=[RegexValidator(regex='^8[0-9]{10}$', message='Incorrect phone')])

class PhoneForm(ModelForm):
    class Meta:
        model = ThePhone

        content = forms.IntegerField(label='Enter your phone')