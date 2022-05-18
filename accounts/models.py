from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    image = models.ImageField( upload_to='Users_profiles_images/%y/%m/%d')

    def __str__(self):
        return f'User Profile: {self.user.first_name} {self.user.last_name}'
    ذ