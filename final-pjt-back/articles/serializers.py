from rest_framework import serializers
from .models import Article, Comment

class ArticlelistSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Article 
        fields = ('id' , 'title','content','created_at','updated_at','user',)

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Comment
        fields = ('id','content','user',)

class ArticleSerializer(serializers.ModelSerializer):
    # 오버라이딩
    comment_set = CommentSerializer(
        many=True,
        read_only=True
    )
    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True 
    )
    class Meta:
        model = Article
        fields = ('id','title','content','created_at','updated_at', 'comment_set', 'comment_count',)