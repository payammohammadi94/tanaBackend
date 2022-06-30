from django.contrib import admin
from .models import Category,Tablighat,Product,Size,Color,VarientProduct,ImageGallery,Comment,Brand



# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update','is_subcategory')
    list_filter = ('name','create')
    search_fields = ('name',)
    
admin.site.register(Category,CategoryAdmin)


class TablighatAdmin(admin.ModelAdmin):
    list_display = ('name', 'create')
    list_filter = ('name','create')
    search_fields = ('name',)
    
admin.site.register(Tablighat,TablighatAdmin)

class VarientProductInlines(admin.TabularInline):
    model = VarientProduct
    extra=1
    
class ImageGalleryInlines(admin.TabularInline):
    model = ImageGallery
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','amount','unit_price','total_price','discount','sale','brand','create','update','is_varient','total_like','total_favorite','total_view')
    list_filter = ('name','amount','category','brand')
    search_fields = ('name','category','brand')
    list_editable = ('amount','discount')
    
    inlines = (VarientProductInlines,ImageGalleryInlines)
    
admin.site.register(Product,ProductAdmin)
admin.site.register(VarientProduct)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ImageGallery)
admin.site.register(Comment)
admin.site.register(Brand)

