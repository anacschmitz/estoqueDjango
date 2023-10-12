from django.db import models

class Products(models.Model):
  itens = (
    ('1','P'),
    ('2', 'M'),
    ('3', 'G'),
    ('4', 'GG')
  )

  name = models.CharField(max_length=255)
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

