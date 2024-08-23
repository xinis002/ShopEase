
from django.urls import path


from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.views import ProductListView, ProductFormView


app_name = CatalogConfig.name



urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductListView.as_view(), name='product_detail'),
    path('products/<int:pk>', ProductFormView.as_view(), name='product_form'),
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]

