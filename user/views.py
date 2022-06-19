from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password

from django.views.decorators.csrf import csrf_exempt

from user.serializers import UserSerializer
from .models import User


class SignUpView(APIView):

    permission_class = [permissions.AllowAny]

    def post(self, request):
        # data = json.loads(request.body)
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        name = request.data.get('name', None)
        email = request.data.get('email', None)
        # User.objects.create(email=email, password=password)

        passcode = make_password(password)
        User(username=username, password=passcode, name=name, email=email).save()

        return Response({"massage": f"회원가입이 완료되었습니다. {username}님 환영합니다!"}, status=status.HTTP_200_OK)


class UserView(APIView):
    @csrf_exempt
    def get(self, request):
        user = request.user
        serialized_user_data = UserSerializer(user).data
        return Response(serialized_user_data, status=status.HTTP_200_OK)


    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)


    def delete(self, request):
        logout(request)
        return Response({"message": "로그아웃 성공!!"})


    

    