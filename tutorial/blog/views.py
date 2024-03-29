from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from blog.models import Article
from datetime import datetime

# Create your views here.

def Test(request):
    #post = Article.objects.all()
    #return HttpResponse(post[0].content)
    return render(request,'test.html',{'current_time': datetime.now()})

def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request,'home.html',{'post_list':post_list})

def Detail(request,id):
    try:
        post = Article.objects.get(id = str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,"post.html",{"post":post})
    