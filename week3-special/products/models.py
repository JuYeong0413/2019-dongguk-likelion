from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200) #charfield는 문자열이라는 속성, 반드시 최대길이를 적어줘야한다
    price = models.IntegerField()
    description = models.TextField() #column.. 그리고 타입
    
    #datetime과 date가 있음. datetime은 시간도 알려주지만 date는 날짜만 알려줌
    created_at = models.DateTimeField(auto_now_add = True)
    #modeling을 통해서 얻게 된 모델의 오브젝트를 생성할 때 자동으로 created_at이 지금 시간으로 기록된다
    updated_at = models.DateTimeField(auto_now = True)
    