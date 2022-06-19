from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('', views.UserView.as_view()),

    path('login/', views.UserView.as_view()),
    path('logout/', views.UserView.as_view()),
    
    path('signup/', views.SignUpView.as_view()),
]
