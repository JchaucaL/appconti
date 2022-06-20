#from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
STATUS_CHOICES = (
    ('BOUGHT', 'Bought'),
    ('PENDING', 'Pending'),
    ('NOT AVAILABLE', 'Not Available'),
)
class Item(models.Model):
    name = models.CharField(max_length=127)
    quantity = models.CharField(max_length=63)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='PENDING')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Codigo   = models.CharField(max_length=12, default=' ')

    
class Escalas(models.Model):
    Codigo   = models.CharField(max_length=12)
    Unidad   = models.CharField(max_length=10)
    Descrip  = models.CharField(max_length=127)
    Cantidad = models.CharField(max_length=12)
    Descto   = models.CharField(max_length=12)
    Valor_Vta= models.CharField(max_length=12)
    Prec_Fin = models.CharField(max_length=12)
    Stock    = models.CharField(max_length=12)

