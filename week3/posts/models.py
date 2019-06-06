from django.db import models

# Create your models here.
class Post(models.Model): #괄호 안에 있는 건 상속받는 것. models.Model 반드시 써줘야 함
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #post에 해당하는 게시글이 생성되면 created_at이 자동으로 post가 생성된 시간으로 데이터 저장
    updated_at = models.DateTimeField(auto_now=True) #auto now add는 게시글 생성하자마자 현재시간 바로 들어가는 것
    #auto now는 수정할때마다 현재시간이 바로 들어가는 것
    #이거 쓰고 python manage.py makemigrations