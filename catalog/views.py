from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


class ProductListView(ListView):
    model = Product


class ProductFormView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.viwes_counter += 1
        self.object.save()
        return self.object




class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category', 'manufactured_at')
    success_url = reverse_lazy('catalog:product_detail')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category', 'manufactured_at')
    success_url = reverse_lazy('catalog:product_detail')

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    fields = ('name', 'description', 'price', 'image', 'category', 'manufactured_at')
    success_url = reverse_lazy('catalog:product_list')

