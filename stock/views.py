from django.shortcuts import render
from .models import Product

def product_list(request):
# بنجيب كل المنتجات من الداتا بيز
    products = Product.objects.all()
# بنبعتها لصفحة الـ HTML اللي هنعملها
    return render(request, 'stock/product_list.html', {'products': products})