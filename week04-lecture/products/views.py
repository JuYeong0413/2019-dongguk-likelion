from django.shortcuts import render, redirect, get_object_or_404
# 404는 not found error의 코드, 어떤 페이지가 없을 때 404라는 에러를 보여준다. 즉, 페이지가 없다는 걸 보여줌
from .models import Product

# Create your views here.
def list(request):
    products = Product.objects.all()
    
    return render(request, 'products/list.html', {'products': products})
    
    
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        product = Product(title=title, price=price, description=description, image=image) #담기만 한 것
        # product = Product.objects.create(title=title, price=price, description=description) #담기만 한 것
        product.save() #객체 하나가 생성됨
        return redirect('list')
        
    return render(request, 'products/create.html')
    
    
def show(request, id):
    # 2를 이용해서 Product에서 pk(id)가 2인 녀석을 찾아서 이 녀석을 show.html에 던져주자
    product = get_object_or_404(Product, pk=id)
    default_view_count = product.view_count
    product.view_count = default_view_count + 1
    product.save()
    return render(request, 'products/show.html', {'product': product})


def edit(request, id):
    product  = get_object_or_404(Product, pk=id)
    return render(request, 'products/edit.html', {'product': product})


def update(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=id)
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        product.title = title
        product.price = price
        product.description = description
        product.save()
        return redirect('products:show', product.pk)


def delete(request, id):
    if request.method == "POST":
        product = Product.objects.get(pk=id)
        product.delete()
        return redirect('list')
        
        
