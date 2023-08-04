from django import forms
from hammer_test.authorization.models import Phones_n_codes


class CodeForm(forms.ModelForm):
    entered_code = forms.CharField(max_length=6)
    class Meta:
        model = Phones_n_codes
        fields = ['entered_code']