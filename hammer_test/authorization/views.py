from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Phones_n_codes
from .forms import PhoneForm
import time


@require_http_methods(['GET'])
def authorization(request):
    form = PhoneForm()
    return render(request, 'authorization.html', {'form': form})


@require_http_methods(['GET'])
def enter_code(request):
    form = PhoneForm(request.GET)
    is_exist = Phones_n_codes.objects.filter(phone=request.GET.get("phone")).exists()
    time.sleep(2)
    if is_exist:
        status = 'exists'
        return render(
            request,
            'enter_code.html',
            {'form': form, 'phone': request.GET.get("phone"), 'status': status}
        )
    status = 'not_exists'
    return render(
        request,
        'enter_code.html',
        {'form': form, 'phone': request.GET.get("phone"), 'status': status}
    )
