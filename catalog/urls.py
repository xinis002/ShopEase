
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, ProductUpdateView, ProductDeleteView, HomeView, BlogPostListView, \
    BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView
from catalog.views import ProductListView, ProductFormView, ContactsView


app_name = CatalogConfig.name



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='product_detail'),
    path('products/<int:pk>', cache_page(60)(ProductFormView.as_view()), name='product_form'),
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('blog/', BlogPostListView.as_view(), name='blog_list'),
    path('blog/create/', BlogPostCreateView.as_view(), name='blog_create'),
    path('blog/<slug:slug>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('blog/<slug:slug>/edit/', BlogPostUpdateView.as_view(), name='blog_edit'),
    path('blog/<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='blog_delete')
]

