from django.htpt import HttpResponse 
from django.shortcuts import redirect

def index(request):
    return HttpResponse("index.html")


