from django.urls import path
from . import views

urlpatterns=[
    path('', views.home ,name='home'),
    path('register/', views.register ,name='register'),
    path('register_user/', views.register ,name='register_user'),
    path('users/', views.users, name='users'),
    path('delete_user/<int:id>', views.delete_user, name='delete_user'),
]