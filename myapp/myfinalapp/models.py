from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#basic user model
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_birthday = models.DateField()  # YYYY-MM-DD
    user_balance = models.SmallIntegerField()
    #TODO credits
    def __str__(self):
        return self.user.username

class Credit(models.Model):
    sum_borrowed = models.SmallIntegerField()
    interest = models.SmallIntegerField()
    client = models.OneToOneField(User,on_delete=models.CASCADE,default=1)




