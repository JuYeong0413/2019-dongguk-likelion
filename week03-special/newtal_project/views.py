from django.shortcuts import render
from products.models import Product #product 모델 가져오기

def main(request):
    products = Product.objects.all() #product의 object들의 모든 것을 가져오겠다
    #괄호가 안 붙는 건 ~의, ~것 project의 object들
    #괄호 붙은 건 함수 - 모든것을 불러온다
    
    return render(request, 'main.html', {'products': products}) #main.html을 render 갖고와서 return 출력해라