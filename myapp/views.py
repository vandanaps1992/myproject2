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