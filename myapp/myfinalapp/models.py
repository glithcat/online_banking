from django.db import models

# Create your models here.
#basic user model
class User(models):
    user_name = models.CharField(unique=False, max_length=10)
    user_surname = models.CharField(unique=False, max_length=10)
    user_birthday = models.DateField() #YYYY:MM:DD
    user_balance = models.SmallIntegerField()
    unique_id = models.IntegerField(primary_key=True)
    #TODO this :user_credits =

class credit(models):
    sum_borrowed = models.SmallIntegerField()
    interest = models.SmallIntegerField()
