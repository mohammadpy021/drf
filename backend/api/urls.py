from django.urls import path
from .views import ArticleList, ArticleDetail , UserDetail, UserList, RevokeToken
urlpatterns = [
    path('',ArticleList.as_view(), name="article-list" ),
    # path('<int:pk>',ArticleDetail.as_view(), name="article-detail" ),#.../api/ex:2
    path('<int:pk>/',ArticleDetail.as_view(), name="article-detail" ),#.../api/ex:2/
    path('user/',UserList.as_view(), name="user-list" ),
    path('user/<int:pk>/',UserDetail.as_view(), name="user-detail"),
    path('revoke/',RevokeToken.as_view(), name="revoke-detail"),

]
