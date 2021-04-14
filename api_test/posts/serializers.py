from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','title','url','poster','created']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vote
        fields=['id','post','voter']