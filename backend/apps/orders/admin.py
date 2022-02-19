from django.contrib import admin

# Register your models here.
from .models import Order, OrderItem
from django.db.models.query import  QuerySet

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
        'get_status_display',
        'created',
        'updated',
    ]
    list_filter = ['is_paid', 'status']
    search_fields = ['id', 'email', 'address']
    list_editable = ['is_paid']
    inlines = [OrderItemInline]
    actions = ['make_status_paid']


    @admin.action(description="Обновить статус оплаты")
    def make_status_paid(self, request, queryset: QuerySet):
        queryset.update(is_paid=True)
