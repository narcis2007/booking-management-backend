"""kick_starter_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from bookings.views import BookingViewSet, BookingDetailViewSet,CheckBookingViewSet
from polls.views import QuestionViewSet



router = routers.DefaultRouter()
router.register(r'bookings', BookingViewSet,'booking')
router.register(r'check_booking', CheckBookingViewSet,'check')


#router.register(r'booking_details', BookingDetailViewSet,'details')

#router.register(r'polls', QuestionViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^api/bookings/', include('bookings.urls', namespace='bookings')),



]
