from django.urls import include, path
from . import views

urlpatterns = [
     path('register', views.register, name="register"),
     path('login', views.login1, name='login1'),
     path('logout', views.logout, name='logout'),
    
     
]