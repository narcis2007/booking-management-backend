from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import  Booking, BookingDetails,CheckBooking
from .serializers import BookingSerializer, BookingDetailSerializer,CheckBookingSerializer
class BookingListView(APIView):
    queryset=Booking.objects.all()

    def get(self,request,format=None):
        bookings=[]
        for booking in Booking.objects.all():

            serializer= BookingSerializer(booking, context={'request':request})
            bookings.append(serializer.data)
        return Response(bookings)
    #def post -validare

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetailListView(APIView):
    queryset=BookingDetails.objects.all()

    def get(self,request,format=None):
        bookingDetails=[]
        for bookingDetail in BookingDetails.objects.all():
            serializer= BookingDetailSerializer(bookingDetail, context={'request':request})
            bookingDetails.append(serializer.data)
        return Response(bookingDetails)

class BookingDetailViewSet(viewsets.ModelViewSet):
    queryset = BookingDetails.objects.all()
    serializer_class = BookingDetailSerializer


#refac sa afiseze doar statusul
class CheckBookingListView(APIView):#refac
    queryset=Booking.objects.all()

    def get(self,request,format=None):
        statuses=[]
        for obj in Booking.objects.all():
            serializer= CheckBookingSerializer(obj, context={'request':request})
            statuses.append(serializer.data)
        return Response(statuses)

    '''
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        import ipd;
        ipdb.set_trace()
        code = self.kwargs['code']
        return CheckBooking.objects.filter(code=code)
    '''

class CheckBookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = CheckBookingSerializer




