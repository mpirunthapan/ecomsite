from django.contrib import admin
from .models import Product, Order

admin.site.site_header = "EcomSite Admin"
admin.site.site_title = "EcomSite Admin Portal"
admin.site.index_title = "Welcome to EcomSite Admin"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request, queryset):
        queryset.update(category='default')

    change_category_to_default.short_description = "Default Category"
    list_display = ('name', 'price', 'discount_price', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    actions = ['change_category_to_default']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
