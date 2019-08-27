from django.contrib import admin
from django.urls import path
from . import views
## 해당폴더에서 views.py를 불러온다.

urlpatterns = [
    path('index', views.index, name='index'),
    ##경로 '사이트주소.com/mtvapp/index'로 정하고 views.py에 있는 index함수를 불러오겠다. 그러고 해당 경로를 index로 명명하겠다.
    path('new', views.new, name='new'),
]