from django.contrib import admin
from models import *

# Register your models here.
@admin.site.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
    # list_display = ('id', 'name', 'address', 'phone', 
    #                 'email', 'tg_id', 'tg_login', 
    #                 'date_created', 'source_created')
    # list_filter = ('name',)
    # search_fields = ('name','phone','email', 'tg_id', 'tg_login')

@admin.site.register(Bonus)
class BonusAdmin(admin.ModelAdmin): pass
    # list_display = ('id', 'name', 'value_percent', 
    #                 'max_step_rub', 'count_days_limit')

@admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin): pass
    # list_display = ('id','name', 'images', 'type',
    #                 'price_sell','price_cost','description')
    # list_filter = ('name','price_sell','price_cost','type','description')
    # search_fields = ('name','price_sell','price_cost','type','description')


@admin.site.register(Order)
class OrderAdmin(admin.ModelAdmin): pass
    # list_display = ('id','customer','product','quantity',
    #                 'date_created','date_send')
    # list_filter = ('customer','product','quantity',
    #                'date_created','date_send')