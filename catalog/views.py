from django.shortcuts import render
from django.template.defaultfilters import register
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


def views_contacts(request):
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


@register.filter(name='split')
def split(text, value):
    return text[:value]


@register.filter(name='mediapath')
def mediapath(picture):
    return f'/media/{picture}'


@register.simple_tag
def mediapath(picture):
    return f'/media/{picture}'