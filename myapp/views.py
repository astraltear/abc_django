from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.context import Context
from myapp.models import Article

# Create your views here.
def hello(request):
    name='한국인'
    msg='반가워'
    ss = "<html><body>안녕 %s %s </body></html>"%(name,msg)
    return HttpResponse(ss)

def hello_template(request):
    
#     name ="Hong"
#     t = get_template('hello.html')
#     he = t.render(Context({'name':name}))
#     return HttpResponse(he)
#       or
    name ="KIM"
    return render_to_response('hello.html',{'name':name})

def myapp1(request):
    return render_to_response('my.html')

def myapp2(request):
    return render_to_response('article.html',{'articles':Article.objects.all()})
    
    
    