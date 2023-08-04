from django import forms
from .models import Phones_n_codes

class PhoneForm(forms.ModelForm):
    phone = forms.CharField(max_length=11)
    class Meta:
        model = Phones_n_codes
        fields = ['phone']