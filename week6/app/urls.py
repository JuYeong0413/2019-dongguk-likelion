from django.urls import path
from . import views

app_name='app'
urlpatterns = [
    path('products/', views.products, name="products"),
    path('register/', views.register, name="register"),
    path('create/', views.create, name="create"),
]