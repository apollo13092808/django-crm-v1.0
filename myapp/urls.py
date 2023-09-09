from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.register, name='register'),
]
