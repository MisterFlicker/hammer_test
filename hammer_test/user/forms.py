from django.forms import ModelForm
from hammer_test.authorization.models import Phones_n_codes


class CodeForm(ModelForm):
    class Meta:
        model = Phones_n_codes
        fields = ['entered_code']