from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def products(request):
    products = Product.objects.all()
    return render(request, 'app/products.html', {'products_html': products})


def register(request):
    return render(request, 'app/register.html')


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        product = Product.objects.create(title=title, price=price, description=description, image=image)
        return redirect('app:products')
        
    return render(request, 'app/register.html')