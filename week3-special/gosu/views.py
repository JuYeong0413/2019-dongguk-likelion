from django.shortcuts import render, redirect

# Create your views here.
global eeee

def cccc(request):
    return render(request, 'gosu/aaaa.html')


def ffff(request):
    if request.method == "POST":
        hhhh = request.POST.get('dddd')
        # return redirect('eeee')
        
    return render(request, 'gosu/gggg.html', {'name': hhhh})