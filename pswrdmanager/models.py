from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Passwords(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    website = models.CharField(null=False,max_length=750)
    password = models.TextField(null=False)

    def __str__(self):
        return f'{self.user}, {self.website}'

class ContactModel(models.Model):
    name = models.CharField(max_length=100,null=False)
    email = models.EmailField(max_length=255,null=False)
    message = models.TextField(null=False)
    