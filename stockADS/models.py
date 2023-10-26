from django.db import models

class Categories(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self) -> str:
    return self.name

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

class Products(models.Model):
  itens = [
    ('1','P'),
    ('2', 'M'),
    ('3', 'G'),
    ('4', 'GG')
  ]

  name = models.CharField(max_length=255)
  category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True)
  picture = models.ImageField(blank=False)
  cod = models.IntegerField(unique=True)
  price = models.DecimalField(max_digits=12, decimal_places=2)
  description = models.TextField()
  size = models.CharField(choices=itens, max_length=255)
  qtd = models.IntegerField()
  discount = models.IntegerField()
  created_at = models.DateTimeField()
  in_stock = models.BooleanField(default=False)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Product'
    verbose_name_plural = 'Products'

