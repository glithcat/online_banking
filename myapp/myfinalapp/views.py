from django.shortcuts import render
from django.views import View
from .forms import aaa as reg_form
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
    def post(self,request):
        username = request.POST.get("username")
        print("usrnm: " + username ,"\n" )
        return render(request,"register.html",{"form":self.form})
        


