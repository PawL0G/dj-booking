from django.contrib import admin

# Register your models here.

from .models import Hotel, Booking

admin.site.register(Hotel)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("title", 'origin', 'date_time', 'rating', 'is_published')
