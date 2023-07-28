from django.urls import path
from . import views

app_name = "community"
urlpatterns = [
    path('write/', views.write, name='write'),
    path('', views.posts, name='posts'),
    path('v/<int:num>/', views.view, name = 'view'),
    path('v/<int:num>/commentcreate', views.comment_create, name='comment_create'),
    path('v/<int:num>/commentdelete/<int:cnum>', views.comment_delete, name = 'comment_delete'),
    path('v/<int:num>/modify', views.modify, name = 'modify'),
    path('v/<int:num>/delete/', views.delete, name = 'delete'),
    path('test', views.test, name = 'test'),
]