"""mtv_project URL Configuration

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
##include 라이브러리를 불러온다.
from mtvapp import urls as mtv_urls
## mtvapp/urls.py 을 불러오는데 'mtv_urls'로 이름을 정하겠다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mtvapp/', include(mtv_urls)),
    ##다음경로를 '사이트주소/mtvapp/~' 설정한다.
]
