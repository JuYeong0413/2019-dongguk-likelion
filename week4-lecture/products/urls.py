from django.urls import path
from . import views

app_name="products"
urlpatterns = [
    path('create/', views.create, name="create"),
    path('<int:id>/', views.show, name="show"),
    # id 라는 이름으로 그 타입은 integer로 주소로 값을 전달할 수 있으면 좋겠다.
    # 아 저렇게 넘겨줄 수 있구나, 그럼 저 id를 int type인 id를 views에서 받을 수 있어야겠구나.
    path('edit/<int:id>', views.edit, name="edit"),
    # edit도 특정 객체를 알아야 하기 때문에 주소로 아이디 값을 넘겨줘야 한다
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
]