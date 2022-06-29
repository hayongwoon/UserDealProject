from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

from user.serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
#회원 가입
class SignupView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

#로그아웃 
#다른 회원 정보
#로그인 한 사용자의 구매 목록 get
#로그인 한 사용자의 판매 목록 get
class UserApiView(APIView):
    #로그인
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['username'] == "None": # username required
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)

        response = {
            'success': True,
            'token': serializer.data['token'] # 시리얼라이저에서 받은 토큰 전달
        }
        return Response(response, status=status.HTTP_200_OK)

    #나의 정보
    def get(self, request):
        return Response({'msg':'get success'})

    #회원 정보 수정
    def put(self, request):
        return Response({'msg':'put success'})

    #계정 비활성화
    def delete(self, request):
        return Response({'msg':'delete success'})