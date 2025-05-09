from django.contrib import admin
from .models import Category, Product, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    search_fields = ['name']
    list_display = [ 'name', 'is_active']



admin.site.register(Category)
admin.site.register(Product)  
admin.site.register(Review)





# Register your models here.
 