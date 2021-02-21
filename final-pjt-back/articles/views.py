from django.shortcuts import get_object_or_404
from .models import Article ,Comment

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import (
    ArticlelistSerializer,
    ArticleSerializer,
    CommentSerializer
)

@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-id')
        serialiszer = ArticlelistSerializer(articles, many=True)
        return Response(serialiszer.data)
    else : 
        serialiszer = ArticlelistSerializer(data=request.data)
        if serialiszer.is_valid(raise_exception=True):
            serialiszer.save(user=request.user)
            return Response(serialiszer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer= ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        if article.user != request.user:
            return Response({'error': '권한이 없습니다'} ,status=HTTP_400_BAD_REQUEST)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else :
        if article.user != request.user:
            return Response({'error': '권한이 없습니다'} ,status=HTTP_400_BAD_REQUEST)
        article.delete()
        return Response({'id': article_pk}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_comment(request,article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article,user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments,many=True)
    return Response(serializer.data)

@api_view(['DELETE','PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete_update(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.method =='DELETE':
        comment.delete()
        return Response({'article_id': article_pk, 'comment_id' : comment_pk})
    else :
        serializer = CommentSerializer(comment,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)