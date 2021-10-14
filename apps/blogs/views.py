from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

from rest_framework.permissions import IsAdminUser


class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer    

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
