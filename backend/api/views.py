from django.shortcuts import render
from .serializers import ArticleSerializer, UserSerializer
from blog.models import Blog
from django.contrib.auth.models import User
from rest_framework.generics import  ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from .permissions import IsSuperuser, IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperuserOrStaffReadOnly
class ArticleList(ListCreateAPIView):
    #API endpoint 
    queryset = Blog.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsStaffOrReadOnly, ]
class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly, ]

class UserList(ListCreateAPIView):
    #API endpoint 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ IsSuperuserOrStaffReadOnly]
    # authentication_classes = [BasicAuthentication]

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ IsSuperuserOrStaffReadOnly]
   

# 75eca57ab5e4914bef47625e3af2ce2f8786a1d4