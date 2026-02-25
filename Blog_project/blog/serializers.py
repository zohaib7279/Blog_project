from rest_framework import serializers #  import serializers jo ka rest_framework sa liya ha
from .models import Author, Post # ya models ma sa author aur post ko yaha par upload kiya ha serializers banana ka liya

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'           # this is author serializer


class PostSerializer(serializers.ModelSerializer):
        class Meta:
                model = Post  # this is post serializer
                fields = '__all__'