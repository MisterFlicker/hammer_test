from django.forms import ModelForm
from .models import Phones_n_codes

class PhoneForm(ModelForm):
    class Meta:
        model = Phones_n_codes
        fields = ['phone']