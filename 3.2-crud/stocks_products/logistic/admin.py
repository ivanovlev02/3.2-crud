from django.contrib import admin
from .models import StockProduct, Product

# Register your models here.

#class StockProductAdmin(admin.ModelAdmin):
#   list_display = ('stock', 'product', 'quantity', 'price')
#    list_editable = ('stock', 'product', 'quantity', 'price')
#    list_filter = ('stock',)

#class ProductAdmin(admin.ModelAdmin):
#    list_display = ('title', 'description')
#    list_editable = ('title', 'description')
#    list_filter = ('title',)

#admin.site.register(StockProduct, StockProductAdmin)
#admin.site.register(Product, ProductAdmin)