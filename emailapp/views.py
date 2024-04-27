import email

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, template_name="input.html")

class Send(View):
    def get(self, request):
        subject = "Welcome to email"
        email_message = "Welcome to email"
        from_email = settings.EMAIL_HOST_USER
        to_list = [email]
        send_mail(subject, email_message, from_email, to_list, fail_silently=False)
        return HttpResponse("Email sent")
