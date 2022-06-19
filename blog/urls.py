from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('list', views.ArticleView.as_view()),
    path('post', views.ArticleView.as_view())
]