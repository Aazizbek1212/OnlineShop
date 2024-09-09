from django.shortcuts import render

from shop.models import Product



def home_view(request):
    return render(request, 'index.html')


def shop_view(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products':products})
