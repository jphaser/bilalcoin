from __future__ import absolute_import

from django.conf import settings
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.documentation import include_docs_urls


# To get and refresh token for authenticated api views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


# To documentation api
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from bilalcoin.users.api.views import (UserViewSet, UserRegisterView, UserProfileView, UserVerifyView)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls

# Swgger url to access documentation for api
schema_view = get_schema_view(
   openapi.Info(
      title="Bilalcoin API",
      default_version='v1',
      description="Get Endpoint to Bilalcoin Brokerage Platform. Ensure to get your accessToken/APIKey.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@bilalcoin.net"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Swagger API Documentation routes
urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


urlpatterns += [
    # Token auth geting and refresh with documentation
    # DRF-simplejwt auth token
    path("login/", TokenObtainPairView.as_view(), name="get_token"),
    path("login/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    # Documentation of API
    path("docs/", include_docs_urls(title="Bilalcoin API Documentation"), name="api_documentation"),
    # User Register Views
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("profile/", UserProfileView.as_view(), name="user-profile"),
    path("verify/", UserVerifyView.as_view(), name="user-verify"),
]