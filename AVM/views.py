import http
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    # return HttpResponse('Hello, World!')
    return render(request, 'homePage.html')