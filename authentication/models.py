from operator import mod
from django.db import models

# Create your models here.
class Customer(models.Model):
   first_Name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=250)
   full_name = models.CharField(max_length=50)
   user_name = models.CharField(max_length=50)
   email = models.CharField(max_length=50)
   password = models.CharField(max_length=20)
   createdAt = models.DateTimeField(auto_now_add=True)

   class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

   def __str__(self):
        return self.name