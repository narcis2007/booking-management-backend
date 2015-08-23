__author__ = 'narcis'
from utils import date_formatter
from django.core.mail import send_mail


def send_initial_email(instance,code):
    #instance.was_saved=True cam asa verific atunci cand un booking a fost confirmat
    send_mail('Initial Email','Hello '+instance.first_name+ ' '+instance.last_name+', you can use the code: '+ code+' to check the status of your booking.','booking.internship@gmail.com',[str(instance.email)])

def send_confirmation_email(instance):
    send_mail('Confirmation Email','Hello again '+instance.first_name+ ' '+instance.last_name+', we\'ve just confirmed your booking! Your appointment date and time is: '+str(instance.final_date.year) +'-'+str(instance.final_date.month)+'-'+str(instance.final_date.day)+' '+str(instance.final_date.hour)+':'+str(instance.final_date.minute),'booking.internship@gmail.com',[str(instance.email)])

def send_final_email(instance):
    send_mail('Final Email','Goodbye '+instance.first_name+ ' '+instance.last_name+', we hope you\'ll use our service! ','booking.internship@gmail.com',[str(instance.email)])
