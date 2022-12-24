from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def venky(request):
    return HttpResponse('<h1><marquee>VENKATESH WEDS SATHYA</marquee></h1>')
def gowtham(request):
    return HttpResponse('<h1><marquee>DIE HARD FAN OF PRABHAS</marquee></h1>')