from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('welcome to myapp')


def home(req):
    return render(req, 'home.html')


def new(request):
    return render(request,'new.html')


def grid(req):
    return render(req,'grid.html')


def products(req):
    return render(req,'products.html')


def newpage(req):
    return render(req,'newpage.html')


def productsnew(req):
    return render(req,'productsnew.html')


def javascrpt(req):
    return render(req, 'javascrpt.html')


def func(req):
    return render(req, 'func.html')


def dommdl(req):
    return render(req,'dommdl.html')


def evnodd(req):
    return render(req,'evnodd.html')


def pattern(req):
    return render(req,'pattern.html')


def amstrong(req):
    return render(req,'amstrong.html')


def palindrom(req):
    return render(req,'palindrom.html')


def strpalndrom(req):
    return render(req,'strpalndrom.html')



def validatn(req):
    return render(req,'validatn.html')



def calculator(req):
    return render(req,'calculator.html')



def newcalculator(req):
    return render(req,'newcalculator.html')