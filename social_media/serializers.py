from rest_framework import serializers

from social_media.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "text", "user", "image")
        read_only_fields = ("user",)
