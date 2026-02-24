from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Post
from .serializers import AuthorSerializer, PostSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend]   # ✅ ENABLE FILTERING
    filterset_fields = ['is_published', 'author']   # ✅ QUERY PARAMS