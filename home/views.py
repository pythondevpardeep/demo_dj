from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime

now = datetime.now()


print("date and time =", dt_string)	
def index(request):
    
    msg = "Code Updated at" + now.strftime("%d/%m/%Y %H:%M:%S")
    return HttpResponse(msg, content_type='text/plain')
