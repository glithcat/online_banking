from django.shortcuts import render
from django.views import View
from .forms import aaa
# Create your views here.
def home(request):
    if request.method == 'POST':
        print("click")
    return render(request, 'homepage.html')
def register (request):
    form = aaa 
    return render(request,"register.html",{"form":form})
class Example(View):
    def get(self,request):
        return render(request,"homepage.html")
    def post(self,request):
        return render(request,"homepage.html")