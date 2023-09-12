from django.db import models
# from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # username = None
    email = models.EmailField(unique=True, verbose_name="ایمیل")
    ### USING EMAIL INSTEAD OF USERNAME IN LOGIN ###
    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = [email]
    # def __str__(self):
    #     return self.email
    # # def get_absolute_url(self):
    # #     return reverse("accounts:home")
