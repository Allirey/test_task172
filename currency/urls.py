from django.urls import path
from . import views

app_name = 'currency'

urlpatterns = [
    path('', views.CurrencyListView.as_view(), name='list'),
    path('history/<str:code>/', views.CurrencyHistory.as_view(), name='history'),
]
