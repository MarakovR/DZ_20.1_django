from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, views_contacts, item_products

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', views_contacts, name='contacts'),
    path('<int:pk>/product/', item_products, name='item_products'),

]
