from blog.models import Blog
from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
class UserSerializer(serializers.ModelSerializer): 
    # def to_representation(self, obj):   
    #     return obj.username

    class Meta:
        model = get_user_model()
        # fields =["id", "username", "first_name", "last_name"]
        fields ="__all__"
        # include = ("author",)

        

class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    # author = UserSerializer()                     # depends on "fields" in UserSerializer or to_representation
    # author = UserSerializer(read_only = True)     # depends on "fields" in UserSerializer or to_representation
    # author = serializers.CharField(source='author.username', read_only=True) 
    author_url = serializers.HyperlinkedIdentityField(view_name='api:users-detail')
    author = serializers.SerializerMethodField()
    def get_author(self, obj):
        return obj.author.username # or return {"username": obj.author.username, "first_name" : "obj.author.first_name"}
    class Meta:
        model = Blog
        fields = "__all__"
        # exclude = ("created_at" , "updated_at")
    def validate_title(self, value):
        if value.lower()  in ['django', 'admin']:
            raise serializers.ValidationError("this word is forbiden")
        return value
    
    ## set current user as author
    # def create(self, validated_data): 
    #     request = self.context.get('request', None)
    #     user = Blog.objects.create(author= request.user, **validated_data)
    #     return user

    ## make readOnly the "author" field if user is not superuser
    # def get_fields(self, *args, **kwargs):
    #     fields = super().get_fields(*args, **kwargs)
    #     request = self.context.get('request', None)
    #     if  not request.user.is_superuser  :
    #         fields['author'].read_only = True
    #     return fields
    
    



