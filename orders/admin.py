from django.contrib import admin

# Register your models here.
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'address',
        'is_paid',
        'status',
        'created',
        'updated',
    ]
    list_filter = ['is_paid', 'status']
    search_fields = ['id', 'email', 'address']
    inlines = [OrderItemInline]