from django.shortcuts import render, redirect
from random import *
#import random
import pdb #python debugging

# Create your views here.
def input_name(request):
    return render(request, 'input_name.html')
    

def death(request):
    return render(request, 'death.html')


def get_name(request):
    if request.method == "POST":
        name = request.POST.get('name')
        redirect('get_name')
    return render(request, 'get_name.html', {'name': name})


def check_number(request):
    if request.method == "POST":
        user_number = int(request.POST.get('user_number'))
        #num_list = [1,2,3]
        #computer_number = random.sample(num_list, 1)
        computer_number = randint(1, 3)
        #pdb.set_trace()
        if user_number == computer_number:
            return redirect('success')
        else:
            return redirect('death')
    


def success(request):
    return render(request, 'success.html')