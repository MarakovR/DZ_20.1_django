from django.shortcuts import render

from catalog.models import Product


def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Каталог продуктов'
    }
    return render(request, 'catalog/index.html', context)


def views_contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Продукт'
    }

    return render(request, 'catalog/product.html', context)
