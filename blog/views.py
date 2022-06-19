from unicodedata import category
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from blog.models import Article as ArticleModel, Category

from drf_class.permissions import RegistedMoreThanThreedaysUser


class ArticleView(APIView):
    permission_class = [RegistedMoreThanThreedaysUser]

    def get(self, request):
        user = request.user

        articles = ArticleModel.objects.filter(user=user)
        titles = [article.title for article in articles]

        return Response({"article_list": titles}) 


    def post(self, request):
        user = request.user
        title = request.data.get('title', '')
        category_name =  request.data.get('category_name', '')
        contents = request.data.get('contents', '')

        if len(title) <= 5:
            return Response({"message": "게시글을 작성할 수 없어요! (제목은 5자 이상)"})

        if len(contents) <= 20:
            return Response({"message": "게시글을 작성할 수 없어요! (내용은 20자 이상)"})
        
        if category_name:
            category = [ Category.objects.get(name=name) for name in category_name.split(',') ]
        else:
            return Response({'message': '카테고리를 지정해주세요!'})

        Article(user=user, title=title, category=category, contents=contents).save()
        return Response({"message": "게시물 작성완료!"}, status=status.HTTP_200_OK)