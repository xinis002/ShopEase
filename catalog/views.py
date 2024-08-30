from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .forms import ProductForm, VersionForm, ProductModeratorForm
from .models import Product, BlogPost, Version
from .services import get_products_from_cache


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

    def get_queryset(self):
        return get_products_from_cache()


class ProductFormView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.viwes_counter += 1
        self.object.save()
        return self.object




class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_detail')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_detail')

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data["formset"] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_edit_category') and user.has_perm('catalog.can_description'):
            return ProductModeratorForm
        raise PermissionDenied('You do not have permission to edit this product')




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


