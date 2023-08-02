from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path('', views.main, name='shop_main'),
    path('brands/<str:item>',views.brand, name='brand')
]