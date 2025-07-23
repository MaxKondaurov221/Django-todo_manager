"""
URL configuration for todo_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.shortcuts import render
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
app_name = 'todo_list'

urlpatterns = [
    #path('',views.index_view, name='index'),
    #path('', views.ToDoListIndexView.as_view(), name='index'),
    path('', views.ToDoListIndexView.as_view(), name='index'),
    path('list/', views.ToDoListView.as_view(), name='list'),
    path('done/', views.ToDoListDoneView.as_view(), name='done'),
    path('<int:pk>', views.ToDoDetailView.as_view(), name='detail'),
]
