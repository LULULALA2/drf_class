from rest_framework.permissions import BasePermission
from datetime import timedelta, datetime
from django.utils import timezone

class RegistedMoreThanThreedaysUser(BasePermission):
    """
    가입일 기준 3일 이상 지난 사용자만 접근 가능
    """
    message = '가입 후 3일 이상 지난 사용자만 이용하실 수 있습니다.'
    
    def has_permission(self, request, view):
        user = request.user

        print(f'user join date : {user.join_date}')
        print(f'now date : {datetime.now()}')
        print(f'3 days ago date : {datetime.now() - timedelta(days=3)}')
        return bool(request.user and request.user.join_date < (timezone.now() - timedelta(minutes=3)))