from django.contrib import admin
from .models import *

## Register your models here.
lista = [Plastika,Printer,Proizvodjac]
admin.site.register(lista)