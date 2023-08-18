from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import index
from django.urls import path, include
from catalog.views import views_contacts

app_name = 'catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('contacts/', views_contacts, name='contacts')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
