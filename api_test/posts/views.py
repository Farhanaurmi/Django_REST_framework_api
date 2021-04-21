from django.shortcuts import render
from rest_framework import generics ,  permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import *
from .serializers import *

class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class Postdel(generics.RetrieveDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self,request, *args, **kwargs):
        post=Post.objects.filter(pk=kwargs['pk'], poster=self.request.user)

        if post.exists():
            return self.destroy(request,*args,**kwargs)

        else:
            raise ValidationError('this isn\'t your post')


class VoteList(generics.CreateAPIView,mixins.DestroyModelMixin):
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


    def delete(self,request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            raise ValidationError('You never voted')





    
    


