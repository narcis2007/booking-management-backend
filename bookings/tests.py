from django.test import TestCase
from email import *
from django.core import mail
from models import Booking
# Create your tests here.
class EmailTest(TestCase):
    def test_send_initial_email(self):
        # Send message.
        send_initial_email(Booking('a','b','narcisc2007@gmail.com','12345'),'1q2w3e')

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Initial Email')

    def test_send_confirmation_email(self):
        # Send message.
        send_confirmation_email(Booking('a','b','narcisc2007@gmail.com'))

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Confirmation Email')

    def test_send_final_email(self):
        # Send message.
        send_final_email(Booking('a','b','narcisc2007@gmail.com','12345'))

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Final Email')

#teste pentru crud