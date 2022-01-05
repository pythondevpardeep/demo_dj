from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    msg="Success"
    return HttpResponse(msg, content_type='text/plain')
