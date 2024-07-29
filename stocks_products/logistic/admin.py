from django.contrib import admin
from .models import StockProduct, Product, Stock

# Register your models here.


class StockAdmin(admin.ModelAdmin):
    list_display = ('address', 'products')
    list_filter = ('address',)


class StockProductAdmin(admin.ModelAdmin):
    list_display = ('stock', 'product', 'quantity', 'price')
    list_filter = ('stock',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title',)


admin.site.register(StockProduct, StockProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)
