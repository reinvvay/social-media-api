from django.db.models import Q
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from social_media.models import Post
from social_media.permissions import IsOwnerOrReadOnly
from social_media.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.filter(Q(user=user) | Q(user__in=user.following.all()))

        username = self.request.query_params.get("username")
        if username:
            queryset = queryset.filter(content__icontains=username)

        return queryset.order_by("-created_at")

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="username",
                description="Filter posts by username mention in content (case-insensitive).",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="ordering",
                description='Ordering by fields like "created_at". Prefix with "-" for descending.',
                type=OpenApiTypes.STR,
                enum=["created_at", "-created_at"],
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        """
        Get posts of the current user and users they follow.

        - Filter by `username` (appears in post content).
        - Order by creation date (`created_at`).
        """
        return super().list(request, *args, **kwargs)
