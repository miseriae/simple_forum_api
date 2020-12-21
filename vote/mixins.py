from rest_framework.decorators import action
from rest_framework.response import Response

from . import services


class LikedMixin:
    @action(detail=True, methods=["POST"])
    def upvote(self, request, pk=None):
        obj = self.get_object()
        services.upvote(obj, request.user)
        return Response()

    @action(detail=True, methods=["POST"])
    def downvote(self, request, pk=None):
        obj = self.get_object()
        services.downvote(obj, request.user)
        return Response()
