"""adventure_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views, urls
from real import urls as really_urls
from adventures import urls as adventures_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"), #이 주소에 접속을 하면 서버는 저기에 있다. 특정 경로에 접속했을 때 길을 설명해 주는 것
    path('app/', include(urls)),
    path('real/', include(really_urls)),
    path('adventures/', include(adventures_urls)),
]

#django에서는 css, js, font, img, video 등을 static이라는 것으로 관리한다.