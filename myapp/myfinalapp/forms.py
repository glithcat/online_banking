from django import forms
class aaa (forms.Form):
    username =forms.CharField(label = "username",max_length =10)
    password =forms.CharField(label = "password",widget = forms.PasswordInput)
    email =forms.EmailField(label = "email" )

