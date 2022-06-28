from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from django.db.models import Q

from django.utils import timezone

from drf_class.permissions import IsAdminOrIsAuthenticatedReadOnly
from .serializers import ProductSerializer



class ProductView(APIView):
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]

    def get(self, request):
        time = timezone.now()
        
        qyery = Q(seller=request.user) | Q(end_date__gt=time, is_active=True)
        product_list = Product.objects.filter(qyery)
        
        return Response(ProductSerializer(product_list, many=True).data, status=status.HTTP_200_OK) 

    
    def post(self, request):
        user = request.user

        if user.is_anonymous:
            return Response({"error": "로그인 후 이용해주세요"}, status=status.HTTP_400_BAD_REQUEST)

        # serializer의 data 인자에는 model로 지정 된 테이블의 field:value를 dictionary로 넘겨준다.
        request.data['seller'] = request.user.id
        product_serializer = ProductSerializer(data=request.data)
        # serializer validator를 통과하지 않을 경우 .is_valid()가 False로 return된다.
        if product_serializer.is_valid():
            # validator를 통과했을 경우 데이터 저장
            product_serializer.save()
            return Response({"message": "정상"}, status=status.HTTP_200_OK)
        
        # .errors에는 validator에 실패한 필드와 실패 사유가 담겨져 있다.
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, obj_id):
        product = Product.objects.get(id=obj_id)

        product_serializer = ProductSerializer(product, data=request.data, partial=True)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response({"message": "정상"}, status=status.HTTP_200_OK)