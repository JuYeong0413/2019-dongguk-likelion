from django.shortcuts import render

# Create your views here.
# def index(request):
#     #request는 웹구성에 필요한 내용들을 포함한다.
#     return render(request, 'index.html')
#       #render(request, '화면에 표시할 html')

#where라는 값을 GET 방식으로 가져온다
def index(request):
    where = request.GET['where']
    when = request.GET['when']
    content = {'where' : where, 'when' : when}
    return render(request, 'index.html', content)

def new(request):
    return render(request, 'new.html')