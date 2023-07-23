from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path('', views.main, name='shop_main'),
]