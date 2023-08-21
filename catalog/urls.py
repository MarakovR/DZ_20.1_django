from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, views_contacts, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('product/', product, name='product'),
    path('contacts/', views_contacts, name='contacts')

]
