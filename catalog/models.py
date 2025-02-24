from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    tg_id = models.CharField(max_length=200, null=True)
    tg_login = models.CharField(max_length=200, null=True)
    tg_photo_id = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    source_created = models.Choices(choices=[(1, 'Telegram'), (2, 'Site'), (3, 'VK')], default=1, null=False)

class Bonus(models.Model):
    name = models.CharField(max_length=200, null=False)
    value_percent = models.IntegerField(null=False)
    max_step_rub = models.IntegerField(null=False)
    count_days_limit = models.IntegerField(null=False, default=30)

class Bonuses_Customers(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    bonus = models.ForeignKey(Bonus, on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    date_expired = models.DateTimeField(null=False)

class TypeProduct(models.Model):
    name = models.CharField(max_length=200, null=False)

class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    type = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, null=False)
    price_sell = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    price_cost = models.DecimalField(null=True, decimal_places=2, max_digits=10)

class Order(models.Model):
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    date_send = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)
    is_bonus = models.BooleanField(default=False)
    bonus_percent = models.IntegerField(null=True)
    bonus_value_rub = models.IntegerField(null=True)
    source_created = models.Choices(choices=[(1, 'Telegram'), (2, 'Site'), (3, 'VK')], default=1, null=False)
    description = models.TextField(null=True)

class Order_Product(models.Model):
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    count = models.IntegerField(null=False)
    