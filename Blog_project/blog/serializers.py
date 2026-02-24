from enum import unique
from rest_framework import serializers
from .models import Author, Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)   # response ke liye
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title empty nahi ho sakta")
        return value

    def validate_content(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Content kam az kam 10 characters ka hona chahiye")
        return value