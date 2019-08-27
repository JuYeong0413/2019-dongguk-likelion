from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request, 'app/one.html')
    

def two(request):
    return render(request, 'app/two.html')


def three(request):
    return render(request, 'app/three.html')