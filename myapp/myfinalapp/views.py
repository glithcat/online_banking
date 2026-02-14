from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from .forms import aaa as reg_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'POST':
        print("click")
    return render(request, 'homepage.html')
class Example(View):
    def get(self,request):
        return render(request,"homepage.html")
    def post(self,request):
        return render(request,"homepage.html")
class Register (View):
    form = reg_form
    def get(self,request):
        return render(request,"register.html",{"form":self.form})

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        print(username)
        print(password)
        print(email)
        return register_or_login_user(request, username, password, email)
class Account (View):
    def get(self,request):
        return render(request,"account.html")
def register_or_login_user(request, username, password, email=None):

    user = authenticate(request=request, username=username, password=password)
    new_acc = request.POST.get("new_account")
    if user is not None:
        print("a")
        login(request, user)
        return redirect("account")   # краще redirect
        # Якщо користувач не знайдений
        # І чекбокс НЕ натиснутий → помилка
    if not new_acc:
        messages.error(request, "Користувача не існує. Хочете створити акаунт?")
        return redirect("reg")
    # якщо не вдалося залогінити — пробуємо створити
    try:
        print("b")
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        print("b1")
        login(request, user)
        messages.error(request,"успішно создано новий аккаунт")
        return redirect("account")

    except IntegrityError:
        print("c")
        messages.error(request, "Користувач з таким іменем вже існує")
        return redirect("reg")