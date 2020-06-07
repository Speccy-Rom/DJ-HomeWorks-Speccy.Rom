from django.shortcuts import render
from .models import Phone
from django.views.generic import ListView


class PhoneList(ListView):
    model = Phone

def show_catalog(request):
    template = 'catalog.html'
    if request.GET:
        sort = request.GET['sort']
        phone_sort = 'id'
        if sort == 'name':
            phone_sort = 'name'
        elif sort == 'min_price':
            phone_sort = 'price'
        elif sort == 'max_price':
            phone_sort = '-price'

    context = {
        'phones': PhoneList.model.objects.order_by(phone_sort)
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = PhoneList.model.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)

def sort_products(request):
    template = 'catalog.html'
    sort = request.GET['sort']
    if sort == 'abc':
        phone_sort = 'name'
    elif sort == 'min_price':
        phone_sort = 'price'
    elif sort == 'max_price':
        phone_sort = '-price'
    context = {
        'phones': PhoneList.model.objects.order_by(phone_sort)
    }
    return render(request, template, context)