from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def sanitary_ware(request):
    thumnail_image = []
    main_img = None
    model_name = ''
    model_description = ''
    technical_drawings = []
    context = {'dada': 14}
    return render(request, 'pages/sanitary_ware.html', context)

def acrylic_bathtubs(request):
    return render(request, 'pages/acrylic_bathtubs.html')

def water_taps(request):
    return render(request, 'pages/water_taps.html')

def additional_items(request):
    return render(request, 'pages/additional_items.html')
