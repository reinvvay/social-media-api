from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from user.views import (
    UserCreateView,
    UserManageView,
    UserViewSet,
    FollowUserView,
    UnfollowUserView,
    FollowersListView,
    FollowingListView,
)

app_name = "user"

router = DefaultRouter()
router.register("list", UserViewSet)

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path("me/", UserManageView.as_view(), name="manage"),
    path("<int:user_id>/follow/", FollowUserView.as_view(), name="follow"),
    path("<int:user_id>/unfollow/", UnfollowUserView.as_view(), name="unfollow"),
    path("followers/", FollowersListView.as_view(), name="followers"),
    path("followings/", FollowingListView.as_view(), name="followings"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
] + router.urls
