#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    name = "Jay"
    html = "<html><body>Hi %s. It worked.</body></html>" % name
    return HttpResponse(html)
