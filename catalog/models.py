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

class Bonuses_Customer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    bonus = models.ForeignKey(Bonus, on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    date_expired = models.DateTimeField(null=False)

class TypeProduct(models.Model):
    name = models.CharField(max_length=200, null=False)

class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    type = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, null=False)
    price = models.FloatField(null=False)
    count_days_limit = models.IntegerField(null=False, default=30)
    bonus = models.ForeignKey(Bonus, on_delete=models.CASCADE, null=False)
    