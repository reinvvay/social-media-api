from django.urls import path, include
from rest_framework.routers import DefaultRouter

from social_media.views import PostViewSet

app_name = "social_media"

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
