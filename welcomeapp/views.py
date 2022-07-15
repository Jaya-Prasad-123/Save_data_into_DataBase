from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import product
# Create your views here.

def welcome(request):
    return HttpResponse('Welcome to Django')


class productinput(View):
    def get(self,request):
        return render(request,'input.html')

class productinsert(View):
    def get(self,request):
        p_id = int(request.GET["t1"])
        p_name = request.GET["t2"]
        p_cost = float(request.GET["t3"])
        p_mnfdate = request.GET["t4"]
        p_expdate = request.GET["t5"]
        P1 = product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mnfdate,pexdpt=p_expdate)
        P1.save()
        res = HttpResponse("Successfully inserted")
        return res








