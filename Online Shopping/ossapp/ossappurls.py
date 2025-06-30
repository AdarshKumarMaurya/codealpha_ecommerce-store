from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('product/',views.productPage,name='product'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('user/',views.user, name='user'),
    path('orders/',views.orders, name='orders'),

]