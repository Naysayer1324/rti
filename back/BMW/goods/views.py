from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.

# class Catalog(ListView):
#     pass

def catalog(request):
    return render(request, 'goods/catalog.html')
