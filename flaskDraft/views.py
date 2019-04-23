from django.http import HttpResponse
from django.shortcuts import rendering

def home_page(request):
    return HttpResponse("Hello World!")
