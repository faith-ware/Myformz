from xmlrpc.client import ResponseError
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import time
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
import threading
from threading import Thread
from smtplib import SMTPException
# Create your views here.


class EmailThread(threading.Thread):
    def __init__(self, subject, message, sender , recipient):
        self.subject = subject
        self.message = message
        self.recipient = recipient
        self.sender = sender
        threading.Thread.__init__(self)

    def run (self):
        try:
            send_mail(self.subject, self.message, self.sender, [self.recipient])
            return True
        except SMTPException as e:        
            print('There was an error sending an email.')
            return False


def send_html_mail(subject, message, sender , recipient):
    EmailThread(subject, message, sender , recipient).start()

class CollectForm(APIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response({"Hello" : "There"})

    def post(self, request, format=None):
        subject = "Frist email test"
        message = "This is the message bro"
        recipient = 'faithade69@gmail.com'
        sent = send_html_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient)
        if sent:
            print(request.data)
            return Response({"Yo" : "Successful"})
        elif sent == False:
            return Response({"Not" : "Done"})
        return Response({"Status" : "Processing"})