
from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import home, contacts
from catalog.views import product_detail, product_form


app_name = CatalogConfig.name



urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', product_detail, name='product_detail'),
    path('products/<int:pk>', product_form, name='product_form'),
]
