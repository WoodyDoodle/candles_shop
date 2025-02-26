from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
    #list_display = ('id', 'name', 'address', 'phone', 
    #                 'email', 'tg_id', 'tg_login', 
    #                 'date_created', 'source_created')
    # list_filter = ('name',)
    # search_fields = ('name','phone','email', 'tg_id', 'tg_login')

@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin): pass
    # list_display = ('id', 'name', 'value_percent', 
    #                 'max_step_rub', 'count_days_limit')

@admin.register(TypeProduct)
class TypeProductAdmin(admin.ModelAdmin): pass
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #list_display = ('id','name', 'images', 'type',
    #              'price_sell','price_cost','description')
    # list_filter = ('name','price_sell','price_cost','type','description')
    # search_fields = ('name','price_sell','price_cost','type','description')
    readonly_fields = ['preview']

    def preview(self, obj: Product):
        galery = obj.images.all()
        if galery:
            content = ''
            for img in galery:
                img: Image
                content += img.img.url
            return mark_safe(content)
        else:
            return '-'
        #return mark_safe(f'<img src="{obj.images.all()[0].img.url}" style="max-width: 200px;">')
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): pass
    # list_display = ('id','customer','product','quantity',
    #                 'date_created','date_send')
    # list_filter = ('customer','product','quantity',
    #                'date_created','date_send')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin): 
    list_display = ('id','name','preview', 'img')