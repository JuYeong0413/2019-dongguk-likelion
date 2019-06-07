from django.contrib.auth.models import AbstractUser
from django.db.models import *
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    image = ImageField(_("Image of User"), upload_to="img/", default="none/default_profile.jpg")
    following = ManyToManyField("self", related_name='followers', symmetrical=False)
    
    
    # followers = ManyToManyField('self', symmetrical=False) ## 'self' : 자기 자신의 모델(클래스)을 의미함
    # followings = ManyToManyField('self', symmetrical=False)

    # def get_absolute_url(self):
    #     return reverse("users:detail", kwargs={"username": self.username})
    
    
## django.contrib.auth.models 추상화클래스 AbstractUser
## AbstractUser 상속받아서 컬럼 추가하거나 함수 만들어서 사용 가능하다

