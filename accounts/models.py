from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    image = models.ImageField( upload_to='profiles_img/%y/%m/%d',default='defualt.png')
    addres = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return f'User Profile: {self.user} '
    
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):

    if created:
        Profile.objects.create(user = instance)
        email = instance.email
        subject = 'Account successfully created sweis'
        msg = f'Hello {instance.username} Account created successfully sweis team welcome you We thank you {instance.first_name} {instance.last_name} for joining us sent to {instance.email}'

        send_mail(subject, msg,  settings.EMAIL_HOST_USER, [email])
        
        


class SendMSG(models.Model):
    msg  = models.TextField(max_length=5000)
    # user = models.CharField(choices=)

