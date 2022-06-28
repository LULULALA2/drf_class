from dataclasses import fields
from datetime import tzinfo
from rest_framework import serializers
from .models import Product, Review
from django.utils import timezone


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = "__all__"
        extra_kwargs = {'product_id': {'write_only': True}}


class ProductSerializer(serializers.ModelSerializer):
    review_set =  ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ["product_name", "thumbnail", "desc", "registration_date", "end_date", "price", "modified_date", "is_active", "review_set"]
        extra_kwargs = {
            "product_name": {"write_only": True},
            "is_active": {"write_only": True},
        }


    # validate 함수 선언 시 serializer에서 자동으로 해당 함수의 validation을 해줌
    def validate(self, data):
        end_date = data.get("end_date", "")
        if end_date and end_date < timezone.now().date():
            raise serializers.ValidationError(detail={"error": "노출 종료일자를 확인해주세요."})
            
        return data

    def create(self, validated_data):
        # desc = validated_data.pop('desc') + f'\n{timezone.now().date()}에 등록된 상품입니다.'
        # validated_data['desc'] = desc
        product = Product(**validated_data) # kawg : 딕셔너리 형태 풀어서 써줌
        product.save()
        product.desc += f"\n\n{product.registration_date.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다." # microsecond랑 txinfo 빼고 표시하도록 함
        product.save()

        return product

    def update(self, instance, validated_data): # instance 기존의 데이터 / validatede_date 새로운 데이터
        for key, value in validated_data.items(): 
            if key == "desc": # 키가 desc일 경우에
                # created = getattr(instance, key).split("\n")[-1] # 위에서 create했던 문장 가지고 오기
                # value += f"\n\n{created}" # value에 가지고온 문장 붙여주기
                value += f"\n\n{instance.created.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다."
            setattr(instance, key, value)
        instance.save()
        instance.desc = f"{instance.modified_date.replace(microsecond=0, tzinfo=None)}에 수정되었습니다.\n\n + instance.desc"
        instance.save()

        return instance

