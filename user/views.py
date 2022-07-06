from functools import partial
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

from user.serializers import UserSerializer, UserLoginSerializer, ProductSerializer
from user.models import User as UserModel

from product.models import Product as ProductModel


# Create your views here.
class UserApiView(APIView):
    #회원 가입
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    #회원 정보
    def get(self, request):
        user = request.user
        # user = UserModel.objects.get(id=16) #test user
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    #회원 정보 수정
    def put(self, request):
        # user = request.user
        # if user.is_anonymous:
        #     return Response({"error": "로그인 후 수정 가능합니다."}, status=status.HTTP_400_BAD_REQUEST)

        user = UserModel.objects.get(id=16) #test user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #회원 탈퇴 - 계정 비활성화
    def delete(self, request):
        # user = request.user
        user = UserModel.objects.get(id=14) #test user
        UserModel.objects.filter(id=user.id).update(is_active=False) #test user

        return Response({'msg':'계정이 삭제 되었습니다.'})


class UserLoginView(APIView):
    #로그인
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['username'] == "None": # username required
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

        response = {
            'success': True,
            'token': serializer.data['token'] # 시리얼라이저에서 받은 토큰 전달
        }
        return Response(response, status=status.HTTP_200_OK)


# 사용자의 판매 목록
class UserSellingListApiView(APIView):
    def get(self, request, user_id):
        user_products = ProductModel.objects.filter(user=user_id).order_by('-register_date') 
        return Response(ProductSerializer(user_products, many=True).data, status=status.HTTP_200_OK)


# 사용자가 좋아요한 prouducts 보기