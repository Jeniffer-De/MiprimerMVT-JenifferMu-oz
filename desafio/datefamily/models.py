from django.db import models

class Datefamily(models.Model):
    name = models.CharField(max_length=50)   
    age = models.FloatField()
    relationship =models.CharField(max_length=50)
    hobbies = models.CharField(max_length=50)
    description = models.CharField(max_length =150, null = True , blank = True)
    creation_date =models.DateField(auto_now=True, null= True,blank=True)
