from django.contrib.auth import get_user_model
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from social_media.permissions import IsOwnerOrReadOnly
from user.serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserManageView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_object(self):
        return self.request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = get_user_model().objects.all()

        username = self.request.query_params.get("username")
        if username:
            queryset = queryset.filter(username=username)

        first_name = self.request.query_params.get("first_name")
        if first_name:
            queryset = queryset.filter(first_name=first_name)

        last_name = self.request.query_params.get("last_name")
        if last_name:
            queryset = queryset.filter(last_name=last_name)

        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="username",
                description="Filter users by exact username.",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="first_name",
                description="Filter users by exact first name.",
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="last_name",
                description="Filter users by exact last name.",
                type=OpenApiTypes.STR,
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        """
        Retrieve list of users.

        Supports filtering by:
        - `username`
        - `first_name`
        - `last_name`
        """
        return super().list(request, *args, **kwargs)


class FollowUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, user_id):
        target_user = get_object_or_404(get_user_model(), id=user_id)
        request.user.following.add(target_user)
        return Response({"detail": f"You followed {target_user.username}"})


class UnfollowUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, user_id):
        target_user = get_object_or_404(get_user_model(), id=user_id)
        request.user.following.remove(target_user)
        return Response({"detail": f"You unfollowed {target_user.username}"})


class FollowersListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        followers = request.user.followers.all()
        serializer = UserSerializer(followers, many=True)
        return Response(serializer.data)


class FollowingListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        following = request.user.following.all()
        serializer = UserSerializer(following, many=True)
        return Response(serializer.data)
