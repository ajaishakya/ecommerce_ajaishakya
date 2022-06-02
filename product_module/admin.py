from django.contrib import admin

# Register your models here.

from .models import Brand, Category, Product

class BrandAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]
    
    class Meta:
        model = Brand

admin.site.register(Brand, BrandAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]
    
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag","name", "price", "brand", "category",]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand","category",]
    #readonly_fields = ["quantity",]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
