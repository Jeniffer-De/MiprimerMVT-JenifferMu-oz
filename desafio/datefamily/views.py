from django.shortcuts import render
from datefamily.models import Datefamily


def create_family(request):
    new_family = Datefamily.objects.create (name= "Andrea Acevedo",age="30",relationship= "Hermana",hobbies="Dormir", description= "Le gusta viajar y es muy chistosa")
    context ={
        "new_family": new_family
    }   
    return render (request, "template_1.html", context=context)

def list_datefamily (request):
    datefamily = Datefamily.objects.all()
    context ={
    "datefamily": datefamily   
    }
    return render(request, list_datefamily.html, context=context )