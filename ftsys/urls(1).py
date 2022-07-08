"""FTSYS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import re_path as url
from ftsys import views
# from . import views

urlpatterns = [
    path('', views.mainpage , name='table'),
    path('Page2',views.page2),
    path('Page3',views.page3),
    path('Page4',views.page4),
    path('page5',views.page5, name='page5'),
    path('removepage/<int:id>', views.removepage, name='removepage'),
    path('edit/<int:id>', views.edit, name='edit'),
    url('admin/', admin.site.urls),

]