__author__ = 'narcis'
from django.conf import settings


from django.conf.urls import url
from .views import BookingListView, BookingDetailListView,CheckBookingListView

urlpatterns = [
    url(r'^bookings$', BookingListView.as_view(), name='bookings'),
    #url(r'details/$', BookingDetailListView.as_view(), name='booking details'),
    url(r'^check$', CheckBookingListView.as_view(), name='checkbooking'),
    #url('^check_booking/(?P<code>.+)/$', CheckBookingListView.as_view(),name='check'),
]
