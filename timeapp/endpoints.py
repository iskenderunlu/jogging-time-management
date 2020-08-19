from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from core.permissions import CustomViewPermission
from timeapp.models import Post

from timeapp.serializers import PostSerializer, PostUpdateSerializer
from timeapp.filters import PostFilter

class TimingsListCreateEndpoint(generics.ListCreateAPIView):
    model = Post
    serializer_class = PostSerializer
    filter_class = PostFilter

    def get_queryset(self):
        user = self.request.user
        return super(TimingsListCreateEndpoint, self).get_queryset() \
            .filter(user=user)

    def create(self, request, *args, **kwargs):
        request.DATA['user'] = self.request.user.id
        return super(TimingsListCreateEndpoint, self).create(request, *args, **kwargs)


class TimingsRetrieveUpdateDestroyEndpoint(generics.RetrieveUpdateDestroyAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, CustomViewPermission)

    def custom_object_permission(self, request, obj=None):
        return request.user == obj.user

    def update(self, request, *args, **kwargs):
        self.serializer_class = PostUpdateSerializer
        return super(TimingsRetrieveUpdateDestroyEndpoint, self).update(request, *args, **kwargs)
