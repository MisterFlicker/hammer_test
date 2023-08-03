from django.shortcuts import render
from hammer_test.authorization.models import Phones_n_codes
from django.views.decorators.http import require_http_methods
from .forms import CodeForm
from hammer_test.authorization.forms import PhoneForm
import random
import string
from django.contrib import messages


def generate_code():
    composition = string.ascii_letters + string.digits
    rand_code = ''.join(random.sample(composition, 6))
    return rand_code


@require_http_methods(['GET', 'POST'])
def user_profile(request, phone):

    if request.method == 'POST' and ("form1" not in request.POST):
        form = PhoneForm(request.POST)
        if form.is_valid():
            new_phone = form.save(commit=False)
            new_phone.self_code = generate_code()
            new_phone.save()
            phone_n_codes = Phones_n_codes.objects.get(phone=phone)
            self_code = phone_n_codes.self_code
            new_form = CodeForm()
            return render(
                request,
                'user_profile.html',
                {
                    'form': new_form,
                    'phone': phone,
                    'entered_code': '',
                    'self_code': self_code,
                    'other_phones': '',
                }
            )
        else:
            return render(request, 'enter_code.html', {'form': form})

    phone_n_codes = Phones_n_codes.objects.get(phone=phone)
    self_code = phone_n_codes.self_code
    if Phones_n_codes.objects.filter(entered_code=self_code).exists():
        other_phones = Phones_n_codes.objects.filter(entered_code=self_code)
        list_of_phones = []
        for i in list(other_phones.values('phone')):
            list_of_phones.append(i['phone'])
    else:
        list_of_phones = ''

    if request.method == 'POST' and "form1" in request.POST:
        form = CodeForm(request.POST, instance=phone_n_codes)
        if Phones_n_codes.objects.filter(self_code=request.POST.get('entered_code')).exists():
            if form.is_valid():
                form.save()
                entered_code = phone_n_codes.entered_code
                return render(
                    request,
                    'user_profile.html',
                    {
                        'form': form,
                        'phone': phone,
                        'entered_code': entered_code,
                        'self_code': self_code,
                        'other_phones': list_of_phones,
                    }
                )
            else:
                return render(
                    request,
                    'user_profile.html',
                    {
                        'form': form,
                        'phone': phone,
                        'entered_code': '',
                        'self_code': self_code,
                        'other_phones': list_of_phones,
                    }
                )
        else:
            messages.error(request, "This code doesn't exist.")
            return render(
                request,
                'user_profile.html',
                {
                    'form': form,
                    'phone': phone,
                    'entered_code': '',
                    'self_code': self_code,
                    'other_phones': list_of_phones,
                }
            )

    if request.method == 'GET':
        form = CodeForm(request.GET)
        if phone_n_codes.entered_code:
            entered_code = phone_n_codes.entered_code
        else:
            entered_code = ''
        return render(
            request,
            'user_profile.html',
            {
                'form': form,
                'phone': phone,
                'entered_code': entered_code,
                'self_code': self_code,
                'other_phones': list_of_phones,
            }
        )
