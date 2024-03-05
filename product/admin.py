from django.contrib import admin
from . models import Size, Color,Product, Category,  Review

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'display_categories', 'stock', 'display_sizes', 'display_colors']

    def display_categories(self, obj):
        return ', '.join([category.name for category in obj.category.all()])
    display_categories.short_description = 'Categories'

    def display_sizes(self, obj):
        return ', '.join([size.name for size in obj.size.all()])
    display_sizes.short_description = 'Sizes'

    def display_colors(self, obj):
        return ', '.join([color.name for color in obj.color.all()])
    display_colors.short_description = 'Colors'



class SizeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}


class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}



admin.site.register(Category)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)