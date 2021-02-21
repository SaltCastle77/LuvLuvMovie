from django.shortcuts import render
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
  HTTP_400_BAD_REQUEST,
  HTTP_201_CREATED,
)
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
  password = request.data.get('password')
  password_confirmation = request.data.get('passwordConfirmation')
  # 비밀번호 일치 확인
  if password != password_confirmation:
    return Response({'error': '비밀번호가 다릅니다'}, status=HTTP_400_BAD_REQUEST)
  # 회원가입
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    user = serializer.save()
    user.set_password(password)
    user.save()
    return Response(serializer.data, status=HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_username(request):
    return Response(request.user.username)