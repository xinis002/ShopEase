from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.CharField(
        max_length=100, verbose_name="Описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="product/photo",
        verbose_name="Изображение",
        help_text="Вставть изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )

    viwes_counter = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за покупку"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания (записи в БД)"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения (записи в БД)"
    )
    manufactured_at = models.DateField(
        null=True, blank=True, verbose_name="Дата производства продукта"
    )

    owner = models.ForeignKey(User, verbose_name="owner", help_text="Owner", blank=True, null=True, on_delete=models.SET_NULL)





    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    preview_image = models.ImageField(upload_to="blog_previews/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продукт",
    )
    number_of_version = models.PositiveIntegerField(
        verbose_name="Номер версии",
        help_text="Укажите номер версии продукта",
        default=0,
        null=True,
        blank=True,
    )
    name_of_version = models.CharField(max_length=255)
    current_version_flag = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
        ordering = ["-number_of_version"]
        unique_together = ["product", "number_of_version"]


        def __str__(self):
            return f"{self.product.name} - версия {self.number_of_version}"

