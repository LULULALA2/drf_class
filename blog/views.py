from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from blog.models import Article

from drf_class.permissions import IsAdminOrIsAuthenticatedReadOnly
from django.utils import timezone


class ArticleView(APIView):
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]

    def get(self, request):
        time = timezone.now()
        articles = Article.objects.filter(user=request.user, startdate__lte=time, enddate__gt=time).order_by('-created_date')
        titles = [article.title for article in articles]
        for article in articles:
            if article.enddate > time:
                titles.append(article.title)

        return Response({"article_list": titles}) 


    def post(self, request):
        user = request.user
        title = request.data.get('title', '')
        category =  request.data.get('category', [])
        contents = request.data.get('contents', '')

        if len(title) <= 5:
            return Response({"message": "게시글을 작성할 수 없어요! (제목은 5자 이상)"}, status=status.HTTP_400_BAD_REQUEST)

        if len(contents) <= 20:
            return Response({"message": "게시글을 작성할 수 없어요! (내용은 20자 이상)"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not category:
            return Response({'message': '카테고리를 지정해주세요!'}, status=status.HTTP_400_BAD_REQUEST)

        new_article = Article(user=user, title=title, contents=contents)
        new_article.save()
        new_article.category.add(*category)
        return Response({"message": "게시물 작성완료!"}, status=status.HTTP_200_OK)