from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('currency.urls', namespace='currency')),
    path('admin/', admin.site.urls),
]
