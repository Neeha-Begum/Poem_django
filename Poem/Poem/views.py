from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def func1(request,name1,name2):
    return HttpResponse(f"<p>{name2}: {name1} {name1}<br>{name1}: Yes papa<br>{name2}: Eating sugar?<br>{name1}: No papa<br>{name2}: Telling lies?<br>{name1}: No papa<br>{name2}: Open your mouth<br>{name1}: HA HA HA")