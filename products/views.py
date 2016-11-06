from django.shortcuts import render

from .models import Category, Product

def home(request):
    return render(request, 'pages/home.html')

def sanitary_ware(request):
    category = Category.objects.get(name='Sanitary Ware')
    products = category.products.all()
    return render(request, 'pages/sanitary_ware.html', {'products': products})

def acrylic_bathtubs(request):
    category = Category.objects.get(name='Acrylic Bath Tubs')
    products = category.products.all()
    return render(request, 'pages/acrylic_bathtubs.html', {'products': products})

def water_taps(request):
    category = Category.objects.get(name='Water Taps')
    products = category.products.all()
    return render(request, 'pages/water_taps.html', {'products': products})

def additional_items(request):
    category = Category.objects.get(name='Additional Items')
    products = category.products.all()
    return render(request, 'pages/additional_items.html', {'products': products})

