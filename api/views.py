from rest_framework import serializers, viewsets
from blog.models import Post
from api.permissions import IsAuthororReadonly
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, UserSerializer

class postviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthororReadonly,]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserviewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
