from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend # ya ma na chatgpt sa liya ha
from .models import Author, Post # ya ma na models sa liya ha jo ma na models.py ma banaya ha
from .serializers import AuthorSerializer, PostSerializer # ya ma na serializers sa liya ha jo ma na serializers.py ma banaya ha


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all() # is sa author ki query set ban jata ha jis ki madad sa ham author ki all objects show kara raha ha
    serializer_class = AuthorSerializer # is sa ham author serializer ko use kar raha ha jo ma na serializers.py ma banaya ha


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all() # is sa post ki query set ban jata ha jis ki madad sa ham post ki all objects show kara raha ha
    serializer_class = PostSerializer # ya bilkul author viewset ki tarah ha bas is ma post serializer use kar raha ha jo ma na serializers.py ma banaya ha

    filter_backends = [DjangoFilterBackend]   # ya ma na chatgpt sa liya ha
    filterset_fields = ['is_published', 'author']   # ya ma na chatgpt sa liya ha