from rest_framework import serializers
from .models import Post

from timeapp.timing_conversion import (from_formated_to_seconds, from_seconds_to_formated)

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        # fields = ('title','time', 'distance', 'date', 'author')
        fields = ('title', 'time', 'distance', 'date')

class PostUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title','time', 'distance', 'date')