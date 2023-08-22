from django.shortcuts import render
from django.template.defaultfilters import register

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


def item_products(request, pk):
    context = {
        'object_list': Product.objects.filter(pk=pk),
        'title': 'Продукт'
    }

    return render(request, 'catalog/product.html', context)


@register.filter(name='split')
def split(text, value):
    return text[:value]


@register.filter(name='mediapath')
def mediapath(picture):
    return f'/media/{picture}'


@register.simple_tag
def mediapath(picture):
    return f'/media/{picture}'
