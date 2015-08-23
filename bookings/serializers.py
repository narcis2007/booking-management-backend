__author__ = 'narcis'
from .models import Booking, BookingDetails,CheckBooking
from rest_framework import serializers
from datetime import datetime
from utils import date_formatter
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        #fields= ('first_name','last_name','email','phone_number','age','sex','cnp','date1','date2','date3','description','clinic')
        fields= ('clinic','first_name','last_name','email','phone_number','age','sex','cnp','date1','date2','date3','description')
    '''
    def validate(self, attrs):
        for i in self.initial_data:

            if i=='age' and (int(self.initial_data[i])>150 or int(self.initial_data[i])<0) :
                raise serializers.ValidationError('invalid age(0-150)')

            if i=='phone_number':
                try:
                    int(self.initial_data[i])
                except  :
                    raise serializers.ValidationError('the phone number must be a number')

            if i=='cnp':
                try:
                    int(self.initial_data[i])
                except  :
                    raise serializers.ValidationError('the cnp must be a number')

            if i=='sex' and self.initial_data[i].upper()!='M' and self.initial_data[i]!='F':
                raise serializers.ValidationError('invalid sex (Ff/Mm)')

            if i == 'first_name' and int(len(self.initial_data[i]))<3:  #de facut:verific daca sunt cifre in last si first name
                raise serializers.ValidationError('First name is too short')

            if i == 'last_name' and int(len(self.initial_data[i]))<3:
                raise serializers.ValidationError('Last name is too short')

            if i == 'phone_number' and int(len(self.initial_data[i]))!=10:
                raise serializers.ValidationError('The mobile phone number should have just 10 digits')

            if i == 'phone_number' and self.initial_data[i][0]!='0':
                raise serializers.ValidationError('The mobile phone number should start with 0')

            if i == 'cnp' and int(len(self.initial_data[i]))!=13 :
                raise serializers.ValidationError('CNP must have 13 digits')

            d1=[]   #formatare: [[an,luna,zi],[ora,minut]]
            d2=[]
            d3=[]
            for i in self.initial_data:#mai trebuie sa testez ca anii sa nu fie din trecut(<2014)
                if i=='date1' :
                    d1=date_formatter(self.initial_data[i])
                if i=='date2' :
                    d2=date_formatter(self.initial_data[i])
                if i=='date3' :
                    d3=date_formatter(self.initial_data[i])
            if d1==d2 or d1==d3 or d2==d3:
                raise serializers.ValidationError('Dates must be different!')

            self.validate_dates(d1, d2, d3)
        return attrs
    '''
    def validate_dates(self, d1, d2, d3):
        ok=0
        year = datetime.now().year
        year1 = int(d1[0][0])
        year2 = int(d2[0][0])
        year3 = int(d3[0][0])
        if year > year1 or year > year2 or year > year3:
            raise serializers.ValidationError('Years must not be in the past!')

        month = datetime.now().month
        day=datetime.now().day

        month1 = int(d1[0][1])
        day1=int(d1[0][2])

        month2 = int(d2[0][1])
        day2=int(d2[0][2])

        month3 = int(d3[0][1])
        day3=int(d3[0][2])

        self.validate_date(day, day1, month, month1, year, year1)
        self.validate_date(day, day2, month, month2, year, year2)
        self.validate_date(day, day3, month, month3, year, year3)

    def validate_date(self, day, day1, month, month1, year, year1):
        if year == year1:
            if month > month1:
                raise serializers.ValidationError('Wrong month')
            if month == month1:
                if day > day1:
                    raise serializers.ValidationError('Wrong day')



class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookingDetails
        fields= ('date1','date2','date3','description', 'id')

    def validate(self, attrs):
        #raise serializers.ValidationError(self.initial_data)
        d1=[]   #formatare: [[an,luna,zi],[ora,minut]]
        d2=[]
        d3=[]
        for i in self.initial_data:#mai trebuie sa testez ca anii sa nu fie din trecut(<2014)
            if i=='date1' :
                d1=date_formatter(self.initial_data[i])
            if i=='date2' :
                d2=date_formatter(self.initial_data[i])
            if i=='date3' :
                d3=date_formatter(self.initial_data[i])
        if d1==d2 or d1==d3 or d2==d3:
            raise serializers.ValidationError('Dates must be different!')

        self.validate_dates(d1, d2, d3)
        return attrs

    def validate_dates(self, d1, d2, d3):
        ok=0
        year = datetime.now().year
        year1 = int(d1[0][0])
        year2 = int(d2[0][0])
        year3 = int(d3[0][0])
        if year > year1 or year > year2 or year > year3:
            raise serializers.ValidationError('Years must not be in the past!')

        month = datetime.now().month
        day=datetime.now().day

        month1 = int(d1[0][1])
        day1=int(d1[0][2])

        month2 = int(d2[0][1])
        day2=int(d2[0][2])

        month3 = int(d3[0][1])
        day3=int(d3[0][2])

        self.validate_date(day, day1, month, month1, year, year1)
        self.validate_date(day, day2, month, month2, year, year2)
        self.validate_date(day, day3, month, month3, year, year3)

    def validate_date(self, day, day1, month, month1, year, year1):
        if year == year1:
            if month > month1:
                raise serializers.ValidationError('Wrong month')
            if month == month1:
                if day > day1:
                    raise serializers.ValidationError('Wrong day')

    '''
    def validate_month(self, d1, d2, d3):
        month = datetime.now().month
        month1 = int(d1[0][1])
        month2 = int(d2[0][1])
        month3 = int(d3[0][1])
        if month > month1 or month > month2 or month > month3:
           raise serializers.ValidationError('The month must not be in the past!')

    def validate_year(self, d1, d2, d3):
        year = datetime.now().year
        year1 = int(d1[0][0])
        year2 = int(d2[0][0])
        year3 = int(d3[0][0])
        if year > year1 or year > year2 or year > year3:
            raise serializers.ValidationError('Years must not be in the past!')
    '''

class CheckBookingSerializer(serializers.ModelSerializer):
    status_message = serializers.ReadOnlyField(source='status.message')
    class Meta:
        model=Booking
        fields= ('status_message','code','clinic','first_name','last_name','email','phone_number','age','sex','cnp','final_date','description')
        read_only_fields=('status_message','code','clinic','first_name','last_name','email','phone_number','age','sex','cnp','final_date','description')
