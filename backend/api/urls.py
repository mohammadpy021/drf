from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import (
    # ArticleList,
    # ArticleDetail,
    # UserDetail,
    # UserList,
    # # RevokeToken,
    UserViewSet,
    ArticleViewSet,
)
# urlpatterns = [
#     path('',ArticleList.as_view(), name="article-list" ),
#     # path('<int:pk>',ArticleDetail.as_view(), name="article-detail" ),#.../api/ex:2
#     path('<int:pk>/',ArticleDetail.as_view(), name="article-detail" ),#.../api/ex:2/
#     path('user/',UserList.as_view(), name="user-list" ),
#     path('user/<int:pk>/',UserDetail.as_view(), name="user-detail"),
#     # path('revoke/',RevokeToken.as_view(), name="revoke-detail"),


# ]

router = DefaultRouter()
router.register(r'users', UserViewSet,  basename='users')
router.register(r'', ArticleViewSet, basename='articles')
urlpatterns = router.urls
# urlpatterns = [ 
#     path('', include(router.urls))
# ]