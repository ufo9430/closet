from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('write/', views.write, name='write'),
    path('', views.posts, name='posts'),
    path('view/<int:num>/', views.view),
    path('view/<int:num>/modify', views.modify, name = 'modify'),
    path('view/<int:num>/delete/', views.delete, name = 'delete'),
]