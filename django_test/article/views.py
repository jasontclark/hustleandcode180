#from django.shortcuts import render
#from django.http import HttpResponse
#from django.template.loader import get_template
#from django.template.context import Context
from django.shortcuts import render_to_response
from article.models import Article

# Create your views here.
''' def hello(request):
    name = "Jay"
    html = "<html><body>Hi %s. It worked.</body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "Jay"
    t = get_template('hello.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html) '''

def articles(request):
    return render_to_response('articles.html',
                             {'articles': Article.objects.all() })

def article(request, article_id=1):
    return render_to_response('articles.html',
                             {'article': Article.objects.get(id=article_id) })
