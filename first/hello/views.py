from django.shortcuts import render
from .models import *

#Задание 1.

def task1(request):
    books = Book.objects.filter(is_available=True).order_by('title')
    return render(request, 'index.html', {'books': books})

#Задание 2.

def task2(request):
    id_a = 1
    books = Book.objects.filter(author=id_a).order_by("-publication_year")
    return render(request, 'in.html', {'books': books})

#Задание 3.

from django.db.models import Count, Avg, Min, Max

def task3(request):
    avg_price = Book.objects.aggregate(avg=Avg("price"), minn=Min("price"), maxx=Max('price'))
    return render(request, 'in2.html', {'avg': avg_price})

    
# Задание 4.

def task4(request):
    need = Book.objects.filter(price__gt=1000,  publication_year__lt=1980 ).order_by('-price')
    return render(request, 'in3.html', {'need ': need})