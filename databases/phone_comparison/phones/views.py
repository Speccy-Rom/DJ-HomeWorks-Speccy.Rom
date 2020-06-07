from django.shortcuts import render
from django.views.generic import ListView
from phones.models import Apple, Samsung, Phone


class AppleList(ListView):
    model = Apple
    list = Apple.object.all()[0]

class SamsungList(ListView):
    model = Samsung
    list = Samsung.object.all()[0]

class PhoneList(ListView):
    model = Phone
    list = Phone.object.all()

def show_catalog(request):
    template = 'catalog.html'
    phones = [AppleList.list, SamsungList.list]
    # a = AppleList.list
    # s = SamsungList.list
    # phones = [[]]

    context = {
        'phones': phones
    }
    return render(
        request,
        template,
        context
    )
