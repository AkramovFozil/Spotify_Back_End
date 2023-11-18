from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.username)
