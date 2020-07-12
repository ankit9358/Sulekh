from django.db import models


# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=12)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.email
