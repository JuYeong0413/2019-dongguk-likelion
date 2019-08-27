from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html') #render는 무언가를 띄워주는 것. html, js 등
    #서버에 해당하는 main이라는 request 요청이 날라오면 그 request에 대응해서 render 보여주겠다 main.html
    
    
def holy(request):
    return render(request, 'holy.html')