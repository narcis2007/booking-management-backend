from django.contrib import admin
from .models import Booking, BookingDetails,Clinic,CheckBooking,Status


class BookingAdmin(admin.ModelAdmin):
    list_display = ['code','first_name','last_name','email','status']
    list_filter = ['status']


admin.site.register(Booking,BookingAdmin)
#admin.site.register(BookingDetails)
admin.site.register(CheckBooking)
admin.site.register(Status)
#admin.site.register(Clinic)