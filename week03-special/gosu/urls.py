from django.urls import path
from . import views

# app_name = "gosu"
urlpatterns = [
    path('aaaa/', views.cccc, name='bbbb'), #bbbb는 url에 있는 것과 같은 name, aaaa를 띄워준다음에 cccc로 간다.
    #cccc는 views.py에 있는 것
    path('gosu/', views.ffff, name="eeee"),
]