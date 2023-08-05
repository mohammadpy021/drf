from typing import Any, Optional
from django.db import models
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blog


class ArticleList(ListView):
    queryset = Blog.objects.all()


class ArticleDetail(DetailView):
    # model = Blog
    def get_object(self):
        self.pk = self.kwargs.get("pk")
        # return Blog.objects.get(pk= self.pk)
        return get_object_or_404(Blog, pk= self.pk)
    
    


