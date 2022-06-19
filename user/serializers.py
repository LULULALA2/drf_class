from dataclasses import fields
from rest_framework import serializers
from user.models import User, UserProfile
from blog.models import Article, Comment


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ArticleSerializers(serializers.ModelSerializer):
    
    comment_set = CommentSerializers(many=True)
    
    class Meta:
        model = Article
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["birth", "bio"]


class UserSerializer(serializers.ModelSerializer):

    userprofile = UserProfileSerializer()
    article_set = ArticleSerializers(many=True)

    class Meta:
        # serializer에 사용될 model, field지정
        model = User
        fields = ["username", "name", "email", "join_date", "userprofile", "article_set"]





