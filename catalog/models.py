from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    tg_id = models.CharField(max_length=200, null=True)
    tg_login = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    SOURCE_CHOICES = [
        (1, 'Telegram'),
        (2, 'Site'),
        (3, 'VK'),
    ]
    source_created = models.IntegerField(choices=SOURCE_CHOICES, default=1, null=False)
    #source_created = models.TextChoices(choices=[(1, 'Telegram'), (2, 'Site'), (3, 'VK')], default=1, null=False)

class Bonus(models.Model):
    name = models.CharField(max_length=200, null=False)
    value_percent = models.IntegerField(null=False)
    max_step_rub = models.IntegerField(null=False)
    count_days_limit = models.IntegerField(null=False, default=30)
    
    class Meta:
        verbose_name_plural = 'Bonuses'
        

class Bonuses_Customers(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    bonus = models.ForeignKey(Bonus, on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    date_expired = models.DateTimeField(null=False)

class TypeProduct(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self) -> str:
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=200, null=False)
    img = models.ImageField(upload_to='images/', null=False)

    def preview(self):
        return mark_safe(f'<img src="{self.img.url}" style="height: 100px;" class="product-image">')

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    images = models.ManyToManyField(Image)
    preview_image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, related_name='preview_image')
    type = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, null=False)
    price_sell = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    price_cost = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    description = models.TextField(null=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    date_send = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)
    is_bonus = models.BooleanField(default=False)
    bonus_percent = models.IntegerField(null=True)
    bonus_value_rub = models.IntegerField(null=True)
    #source_created = models.Choices(choices=[(1, 'Telegram'), (2, 'Site'), (3, 'VK')], default=1, null=False)
    SOURCE_CHOICES = [
        (1, 'Telegram'),
        (2, 'Site'),
        (3, 'VK'),
    ]
    source_created = models.IntegerField(choices=SOURCE_CHOICES, default=1, null=False)
    description = models.TextField(null=True)

class Order_Product(models.Model):
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    count = models.IntegerField(null=False)
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    last_add = models.DateTimeField(null=True)
    is_paid = models.BooleanField(default=False)
    products = models.ManyToManyField(Product, through='Cart_Product')

class Cart_Product(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    count = models.IntegerField(default=1, null=False)

    def add_or_update(self, count, *args, **kwargs):
        object_ = Cart_Product.objects.filter(
            cart = self.cart,
            product=self.product
            ).first()
        if object_:
            object_.count = count
            object_.save()
        else:
            new_obj = Cart_Product.objects.create(
                cart = self.cart,
                product = self.product,
                count = count
            )
            new_obj.save()
            