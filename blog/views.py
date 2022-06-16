from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from blog.models import Article as ArticleModel


class ArticleView(APIView):
    permission_class = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = request.user

        articles = ArticleModel.objects.filter(user=user)
        titles = [article.title for article in articles]

        return Response({"article_list": titles}) 
