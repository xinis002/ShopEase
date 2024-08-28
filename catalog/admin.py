from django.contrib import admin
from catalog.models import Category, Product, BlogPost, Version

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "description")
    search_fields = ("name", "description")



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'number_of_version', 'name_of_version')
