from multiprocessing import context
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render 

def family(request):
    return HttpResponse("This is my family.")

def datfamily_template(request):
        return render(request, "template_1.html", context={})
