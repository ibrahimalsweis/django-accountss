from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    image = models.ImageField( upload_to='Users_profiles_images/%y/%m/%d')

    def __str__(self):
        return f'User Profile: {self.user   } '
    
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):

    if created:
        Profile.objects.create(
            user = instance,

        )