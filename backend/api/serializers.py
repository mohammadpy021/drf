from blog.models import Blog
from django.contrib.auth.models import User
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        # exclude = ("created_at" , "updated_at")



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # include = ("author",)
        # exclude = ("created_at" , "updated_at")