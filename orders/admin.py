from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order, OrderItem


class OrderItemTabularInline(admin.StackedInline):
    model = OrderItem
    fields = ['order', 'product', 'count', 'price']
    extra = 1


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin , admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'datetime_created', 'user', 'is_paid', ]
    inlines = [OrderItemTabularInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'count', 'price']