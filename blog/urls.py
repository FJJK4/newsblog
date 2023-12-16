"""
URL configuration for news_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category_detail/<slug:slug>/', views.category_detail, name='category_detail_url'),
    path('post_detail/<slug:slug>', views.post_detail, name='post_detail_url'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login_site, name='login_site'),
    path('log_out/', views.logout_site, name='logout_site'),
    path('post_detail/<slug:slug>/comment', views.comment, name= 'comment'),

]