from django.contrib import admin
from sangpum.models import Maker, Product

# Register your models here.
class MakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'mname', 'tel', 'addr')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'pname', 'price', 'maker_name')
        
admin.site.register(Maker, MakerAdmin)
admin.site.register(Product, ProductAdmin)