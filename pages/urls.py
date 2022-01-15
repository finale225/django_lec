"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from.import views


urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
    path('news/', views.news),
    path('product_all/', views.product_all),
    path('product_detail/', views.product_detail),
    path('newProduct1/', views.newProduct1),
    path('newProduct2/', views.newProduct2),
    path('newProduct3/', views.newProduct3),
    path('ToS/', views.ToS),
    path('privacy_policy/', views.privacy_policy),
]
