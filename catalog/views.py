from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Product, BlogPost


#def home(request):
    #return render(request, 'catalog/home.html')


#def contacts(request):
    #return render(request, 'catalog/contacts.html')


class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'









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






class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'catalog/blog_list.html'
    context_object_name = 'posts'
    queryset = BlogPost.objects.filter(is_published=True).order_by('-created_at')




class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'
    context_object_name = 'posts'

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        post.views += 1
        post.save()
        return post




class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'catalog/blog_form.html'
    fields = ['title', 'content', 'preview_image', 'is_published']
    success_url = reverse_lazy('catalog:blog_list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog_form.html'
    fields = ['title', 'content', 'preview_image', 'is_published']
    success_url = reverse_lazy('blog_list')



class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')


