from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:id>/', views.show, name="show"), #id가 있는데 type은 정수 /posts/show/3
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]