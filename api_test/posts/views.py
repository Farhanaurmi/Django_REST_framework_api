from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

class PostList(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer



class VoteList(generics.ListAPIView):
    queryset=Vote.objects.all()
    serializer_class=VoteSerializer
