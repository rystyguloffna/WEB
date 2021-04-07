from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name='Название')
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    category = models.ForeignKey(Category,related_name="products",on_delete=models.CASCADE)
    name = models.CharField(max_length=200,verbose_name="Название")
    price = models.FloatField(verbose_name="Price")
    description = models.TextField(verbose_name='Description')
    count = models.IntegerField(verbose_name="Count")
    is_active = models.BooleanField(verbose_name="Status",default=False)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"