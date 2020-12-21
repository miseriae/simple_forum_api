from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from .serializers import CommentSerializer
from .models import Comment


#  Rewrite it prob
class CommentView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CreateCommentView(APIView):
    permissions_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user, post=Post.objects.get(pk=pk))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
