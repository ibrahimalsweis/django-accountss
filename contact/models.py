from django.db import models

# Create your models here.
class Info(models.Model):

    location = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return str(self.email)
