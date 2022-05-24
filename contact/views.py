from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):

    info_date = Info.objects.all()
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        # send_mail(
        #     subject, 
        #     message,
        #      email,
        #     ['matrexnat9911@gmail.com'],
        #     )  
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

        print(email)  
        print(settings.EMAIL_HOST_USER)
    return render(request, 'contact/contact.html',{'info_date':info_date})