from django.shortcuts import render
from rest_framework import generics ,  permissions
from rest_framework.exceptions import ValidationError
from .models import *
from .serializers import *

class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class VoteList(generics.CreateAPIView):
    serializer_class=VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        post=Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('you have already voted')
        serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))

    
    


