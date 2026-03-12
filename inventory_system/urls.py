from django.contrib import admin
from django.urls import path
from stock.views import product_list

urlpatterns = [
path('admin/', admin.site.urls),
path('', product_list, name='product_list'),
]