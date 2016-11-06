from django.contrib import admin

from .models import Category, Product, ProductPart

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug')
    list_display = ('name',)
    prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'main_image')

class ProductPartAdmin(admin.ModelAdmin):
    list_display = ('product', 'description', 'image', 'technical_drawing')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPart, ProductPartAdmin)
