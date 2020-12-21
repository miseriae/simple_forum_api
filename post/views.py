from rest_framework import generics, viewsets
from rest_framework import permissions

from vote.mixins import LikedMixin

from .models import Post
from .serializers import PostSerializer


class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Post.objects.all()  # author=self.request.user


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
