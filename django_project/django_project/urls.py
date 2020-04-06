
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecommerce_app.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
]
