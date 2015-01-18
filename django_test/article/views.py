#from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.context import Context

# Create your views here.
def hello(request):
    name = "Jay"
    html = "<html><body>Hi %s. It worked.</body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "Jay"
    t = get_template('hello.html')
    html = t.render(Context({'name': name}))
    
