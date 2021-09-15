from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index') # name 속성은 URL에 이름을 지어서, Django app 어디서든 참조할 수 있도록 하기 위함.
]