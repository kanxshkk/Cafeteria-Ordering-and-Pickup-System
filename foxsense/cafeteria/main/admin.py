from django.contrib import admin

# Register your models here.
# main/admin.py

from django.contrib import admin
from .models import Cafeteria, MenuItem, Order, OrderItem, UserPreferences, Notification, Attendance

@admin.register(Cafeteria)
class CafeteriaAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'cafeteria', 'price', 'is_vegetarian', 'is_vegan', 'is_gluten_free')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'cafeteria', 'order_number', 'status', 'total_amount', 'dining_preference')
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity')

@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = ('user', 'dietary_preference')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'cafeteria', 'timestamp')
