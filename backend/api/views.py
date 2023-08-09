from django.shortcuts import render
from .serializers import ArticleSerializer, UserSerializer
from blog.models import Blog
from django.contrib.auth import get_user_model
from rest_framework.generics import  ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from .permissions import IsSuperuser, IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperuserOrStaffReadOnly
from rest_framework.viewsets import ModelViewSet
# from rest_framework.views import APIView
# from rest_framework.response import Response
class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Blog.objects.all()
    def get_permissions(self):
        if self.action in ['list','create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly ]
        return [permission() for permission in permission_classes]
    
# class ArticleList(ListCreateAPIView):
#     #API endpoint 
#     queryset = Blog.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [IsStaffOrReadOnly, ]
# class ArticleDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [IsAuthorOrReadOnly, ]
#     # permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly ]


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

# class UserList(ListCreateAPIView):
#     #API endpoint 
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [ IsSuperuserOrStaffReadOnly]
#     # authentication_classes = [BasicAuthentication]
# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [ IsSuperuserOrStaffReadOnly]


    

# class RevokeToken(APIView):
#     def get(self, request, format=None):
#         request.user.auth_token.delete()
#         #or request.auth.delete()
#         return Response({"message": "token revoked"})