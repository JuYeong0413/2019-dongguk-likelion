from django.shortcuts import render, redirect
from .models import Product #현재경로의 models안에있는 Product라는 클래스를 가져온 것

# Create your views here.
def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        
        product = Product(name=name, price=price, description=description)
        #name column에 name 집어넣고 price column에 price 집어넣고... -> column 값으로 할당
        product.save()
        return redirect('main')
        
    return render(request, 'products/create.html')