from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.register, name='register'),
    path('customer/<int:pk>/', views.view_customer, name='customer'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('update-customer/<int:pk>/', views.update_customer, name='update_customer'),
    path('delete-customer/<int:pk>/', views.delete_customer, name='delete_customer'),
]
