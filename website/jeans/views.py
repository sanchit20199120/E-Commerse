from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item
# Create your views here.

def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "jeans/home-page.html", context)

def checkout(request):
    return render(request, 'jeans/checkout-page.html')

def product(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'jeans/product-page.html', context)

class HomeView(ListView):
    model = Item
    template_name = "jeans/home-page.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "jeans/product-page.html"