"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from dj_rest_auth.views import PasswordResetConfirmView
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),

    # path('api-auth/', include('rest_framework.urls')), #login in the top right of site
    path('', include('blog.urls')),
    path('api/', include('api.urls')),
    # path('api/token-auth/', obtain_auth_token),

    # path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    # path(# this must be over the line below
    #     'api/dj-rest-auth/registration/account-confirm-email/<key>/',
    #     TemplateView.as_view(template_name="api/account_confirm_email.html"),
    #     name='account_confirm_email',
    # ),
    # path('api/dj-rest-auth/registration/password/reset/confirm/<uidb64>/<token>/',
    #       PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   

]
