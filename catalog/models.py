from django.db import models

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
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за покупку"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания (записи в БД)"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения (записи в БД)"
    )
    manufactured_at = models.DateField(null=True, blank=True, verbose_name='Дата производства продукта')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]

    def __str__(self):
        return self.name



