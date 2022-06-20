from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status
from datetime import timedelta, datetime
from django.utils import timezone


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code = status_code
        super().__init__(detail=detail, code=code)

        
class IsAdminOrIsAuthenticatedReadOnly(BasePermission):
    """
    admin 사용자 이용가능 / 조회는 모든 사용자 가능, 가입 후 7일이상 이용자만 작성가능
    """
    SAFE_METHODS = ('GET',)
    message = '가입 후 7일 이상 지난 사용자만 이용하실 수 있습니다.'

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response = {
                "detail": "로그인한 사용자만 이용가능합니다.",
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)
        if request.method=='GET':
            if user.is_authenticated and user.is_admin:
                return True

            elif user.is_authenticated and request.method in self.SAFE_METHODS:
                return True

            return False

        if request.method=='POST':
            if user.is_authenticated and user.is_admin:
                return True
            print(f'user join date : {user.join_date}')
            print(f'now date : {datetime.now()}')
            print(f'a week ago date : {datetime.now() - timedelta(days=7)}')
            return bool(request.user and request.user.join_date < (timezone.now() - timedelta(days=3))) 