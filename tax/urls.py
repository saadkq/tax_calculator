from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('<int:num>', views.calculate_price, name='calculate_price'),
    path('taxrate/', views.show_tax_rate, name='show_tax_rate'),
]
