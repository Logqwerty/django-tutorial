"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

urlpatterns = [
    # include 함수는 다른 URL config들을 참조할 수 있도록 함.
    # Django가 include 함수를 만나면, 전체 URL 문자열에서 그 시점까지의 부분 URL과 일치하는 부분을 탐색.
    # 그리고 일치하는 부분까지 잘라내고 남은 substring을 include된 URL config로 전달.
    # ex) /polls/, /fun_polls/, /content/polls/ => 남은 substring이 모두 polls.urls로 전달됨.
    path('polls/', include('polls.urls')),
    # 다른 URL 패턴들은 모두 include로 처리해야 하지만, admin.site.urls만 예외
    path('admin/', admin.site.urls), 
]
