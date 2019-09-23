from django.shortcuts import render
from django.http import HttpResponse
from book_hero.models import *


# Create your views here.


# 定义hello视图
def hello(request):
    # return HttpResponse("<b>hello, world</b>")
    book_list = BookInfo.objects.all()
    context = {"list": book_list}
    return render(request, 'book_hero/hello.html', context)


# 定义index视图
def index(request):
    book_list = BookInfo.objects.all()
    context = {"list": book_list}
    return render(request, 'book_hero/index.html', context)


# 定义show视图
def show(request, id):
    book = BookInfo.objects.get(pk=id)
    hero_list = book.heroinfo_set.all()
    context = {"list": hero_list}
    return render(request, 'book_hero/show.html', context)