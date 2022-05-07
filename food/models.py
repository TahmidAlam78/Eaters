from hashlib import blake2b
from turtle import mode
from django.db import models

class Restaurant(models.Model):
   name = models.CharField(max_length=50)
   res_image = models.ImageField(upload_to='resImages',blank = True)
   location = models.CharField(max_length=250)
   description = models.TextField()
   rating = models.IntegerField()
   createdAt = models.DateTimeField(auto_now_add=True)

   class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

   def __str__(self):
        return self.name
   

class Category(models.Model):
   name = models.CharField(max_length=50)
   createdAt = models.DateTimeField(auto_now_add=True)

   class Meta:
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Categories'

   def __str__(self):
        return self.name

class Item(models.Model):
   name = models.CharField(max_length=50)
   restaurant_id = models.ForeignKey(
      Restaurant, on_delete=models.SET_NULL, null=True, related_name='food_restaurant')
   category_id = models.ForeignKey(
      Category,on_delete=models.SET_NULL,null= True,        related_name='food_category')
   price = models.FloatField()
   description = models.TextField()
   res_image = models.ImageField(upload_to='itemImages',blank = True)
   rating = models.IntegerField()
   createdAt = models.DateTimeField(auto_now_add=True)
   
   class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

   def __str__(self):
        return self.name

class Order(models.Model):
   food_id = models.ForeignKey(
      Item, on_delete=models.SET_NULL, null=True, related_name='food_order')
   restaurant_id = models.ForeignKey(
      Restaurant, on_delete=models.SET_NULL, null=True, related_name='order_restaurant')
   customer_id = models.CharField(max_length=50,null=True)
   price = models.FloatField()
   is_added_to_cart = models.BooleanField(default=False)
   is_checkout = models.BooleanField(default=False)
   is_complete = models.BooleanField(default=False)
   cart_added_date = models.DateTimeField(blank=True,null=True)
   checkout_date = models.DateTimeField(blank=True,null=True)
   order_complete_date = models.DateTimeField(blank=True,null=True)
   createdAt = models.DateTimeField(auto_now_add=True)
   
   class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

   def __str__(self):
        return self.name

class Voucher(models.Model):
   code = models.CharField(max_length=30,null=False)
   percentage = models.FloatField()
   max_discount = models.FloatField()
   createdAt = models.DateTimeField(auto_now_add=True)
   
   class Meta:
        verbose_name = 'Voucher'
        verbose_name_plural = 'Vouchers'

   def __str__(self):
        return self.name

class CartOrder(models.Model):
   customer_id = models.CharField(max_length=50,null=False)
   restaurant_id = models.ForeignKey(
      Restaurant, on_delete=models.SET_NULL, null=True, related_name='cart_order_restaurant')
   voucher_id = models.ForeignKey(
      Voucher, on_delete=models.SET_NULL, null=True, related_name='cart_order_voucher')
   total_food_price = models.FloatField(default=0.0)
   voucher_discount = models.FloatField(default=0.0)
   final_food_price = models.FloatField(default=0.0)
   is_complete = models.BooleanField(default=False)
   checkout_date = models.DateTimeField(blank=True,null=True)
   order_complete_date = models.DateTimeField(blank=True,null=True)
   createdAt = models.DateTimeField(auto_now_add=True)
   
   class Meta:
        verbose_name = 'CartOrder'
        verbose_name_plural = 'CartOrders'

   def __str__(self):
        return self.name
class CartOrderItem(models.Model):
   food_id = models.ForeignKey(
      Item, on_delete=models.SET_NULL, null=True, related_name='food_cart_order')
   cart_order_id = models.ForeignKey(
      CartOrder, on_delete=models.SET_NULL, null=True, related_name='cart_order')
   price = models.FloatField(default=0.0)
   createdAt = models.DateTimeField(auto_now_add=True)
   
   class Meta:
        verbose_name = 'CartOrderItem'
        verbose_name_plural = 'CartOrderItems'

   def __str__(self):
        return self.name
        