from django.shortcuts import render
from django.shortcuts import render
from .models import WeatherLog 
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    weather = WeatherLog.objects.all()
    print("",weather)
    return render(request,'chartapp/index.html',{'weather': weather})