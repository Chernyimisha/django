from django.contrib import admin
from .models import Product, Customer, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(volume=0)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'registration_date']
    ordering = ['-registration_date']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'volume', 'description', 'date', 'image']
    ordering = ['price']
    actions = [reset_quantity]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['date_ordered', 'total_price', 'view_products', 'customer', 'date_ordered']
    ordering = ['-date_ordered']
    readonly_fields = ['date_ordered', 'total_price', 'view_products', 'customer', 'date_ordered']


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
