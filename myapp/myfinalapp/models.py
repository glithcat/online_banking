from django.db import models

# Create your models here.
#basic user model
class User(models.Model):
    user_name = models.CharField(unique=False, max_length=10)
    user_surname = models.CharField(unique=False, max_length=10)
    user_birthday = models.DateField() #YYYY:MM:DD
    user_balance = models.SmallIntegerField()
    unique_id = models.IntegerField(primary_key=True)
    #TODO this :user_credits =

class Credit(models.Model):
    sum_borrowed = models.SmallIntegerField()
    interest = models.SmallIntegerField()
    client = models.OneToOneField(User,on_delete=models.CASCADE)




