from django.db import models
from bookings.email import send_initial_email,send_confirmation_email,send_final_email
from django.core.validators import RegexValidator
from django.utils.crypto import get_random_string
class Clinic(models.Model):
    name=models.CharField(max_length=100,default='unknown')
    def __str__(self):
        return self.name

class BookingDetails(models.Model):#e foreign key
    date1=models.DateTimeField('first date',default='0001-01-01T01:01:00Z')
    date2=models.DateTimeField('second date',default='0001-01-01T01:01:00Z')
    date3=models.DateTimeField('third date',default='0001-01-01T01:01:00Z')
    description=models.CharField(max_length=256)

    def __str__(self):
        return 'Booking detail '+str(self.id)+': first date: '+ str(self.date1)+ ' second date: '+str(self.date2)+ ' third date: '+str(self.date3)+' description: '+ self.description
class Status(models.Model):
    message=models.CharField(max_length=20,default='waiting')

    def __str__(self):
        return self.message

class Booking(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    phone_number=models.CharField(max_length=15)
    #age_regex=RegexValidator(regex=r'^([0-9][0-9])$',message="wrong age")
    age=models.IntegerField(default=1)#validators=[age_regex]
    sex=models.CharField(max_length=1)
    cnp=models.CharField(max_length=20,default='1234')
    #bookingdetails=models.ForeignKey(BookingDetails,default=10)


    date1=models.DateTimeField('first date',default='0001-01-01T01:01:00Z')
    date2=models.DateTimeField('second date',default='0001-01-01T01:01:00Z')
    date3=models.DateTimeField('third date',default='0001-01-01T01:01:00Z')
    description=models.CharField(max_length=256,default='no description')


    #clinic=models.ForeignKey(Clinic,default=1)
    clinic=models.CharField(max_length=256,default='unknown')
    status=models.ForeignKey(Status,default=1)
    code=models.CharField(max_length=6,default='123456',primary_key=True)
    final_date=models.DateTimeField('final date',default='0001-01-01T01:01:00Z')

    def save(self, *args, **kwargs):
        if self.code=='123456':
            self.code=get_random_string(length=6)#de facut: verific daca e unic, daca nu generez pana e unic
            repeat=True
            while repeat==True:
                k=0
                for booking in Booking.objects.all():
                    if booking.code==self.code:
                        k=k+1
                if k==2:
                    self.code=get_random_string(length=6)
                else:
                    repeat=False




        if self.status.message=='waiting':
            self.final_date=self.date1
            send_initial_email(self,self.code)
        if self.status.message=='confirmed':
            send_confirmation_email(self)
        if self.status.message=='finalized':
            send_final_email(self)
        super(Booking, self).save(*args, **kwargs) # Call the "real" save() method.

    def get_status_message(self):
            return self.status.message

    def __str__(self):
        return 'Booking '+str(self.code)+':'+ self.first_name+' ' + self.last_name

class CheckBooking(models.Model):#refac
    code=models.CharField(max_length=10,primary_key=True)
    status=models.CharField(max_length=10,default='Wrong code, please enter a valid one')

    def save(self, *args, **kwargs):
        for booking in Booking.objects.all():
            if booking.code==self.code:
                self.status=booking.status
        super(CheckBooking, self).save(*args, **kwargs) # Call the "real" save() method.
    #fac un check status

    def __str__(self):
        return self.code+ ' : ' + self.status


