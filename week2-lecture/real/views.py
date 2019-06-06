from django.shortcuts import render, redirect

# Create your views here.
def first(request):
    return render(request, 'first.html')
    
    
def second(request):
    return render(request, 'second.html')
    
    
def third(request):
    return render(request, 'third.html')
    
    
def fourth(request):
    if request.method == "POST":
        name = request.POST.get('name')
        redirect('fourth') #무조건 get방식으로 날라가게 된다
    return render(request, 'fourth.html', {'name': name})