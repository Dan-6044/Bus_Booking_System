from django.contrib import admin
from .models import Booking, Bus, Payment 

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'bus', 'from_location', 'to_location', 'date', 'seat_number', 'created_at')
    list_filter = ('bus', 'date')  # Filters for the admin list view
    search_fields = ('from_location', 'to_location', 'seat_number')  # Fields to search in admin interface


admin.site.register(Bus)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'bus_name', 'payment_method', 'price', 'created_at')
    search_fields = ('booking__bus__name', 'payment_method', 'booking__seat_number')
    list_filter = ('payment_method', 'created_at')


# Register your models here
admin.site.register(Payment, PaymentAdmin),