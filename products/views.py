from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ a view to show all products and show sorting and searches as well """
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
