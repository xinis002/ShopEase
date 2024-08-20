from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')




def product_detail(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/product_list.html', context)


def product_form(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product_form.html', context)
