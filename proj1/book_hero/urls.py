# @author: huhao
# @file: urls.py
# @time: 2019/9/23 9:15
# @Document：https://www.python.org/doc/
# @desc:

from django.conf.urls import url
from book_hero import views

urlpatterns = [
    url(r'^hello$', views.hello),
    url(r'^index$', views.index),
    url(r'^(\d+)$', views.show),      # 此处加上（）是为了获取正则表达式中的参数
]