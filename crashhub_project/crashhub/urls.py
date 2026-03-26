"""
URL configuration for crashhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include

# DRF Router
from rest_framework.routers import DefaultRouter

# JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Views import
from Users.views import UserViewSet
from victims.views import VictimViewSet

# Router Configuration

router = DefaultRouter()

# Users APIs
router.register(r'users', UserViewSet, basename='users')

# Victims APIs (IMPORTANT)
router.register(r'victims', VictimViewSet, basename='victims')


# ========================
# Swagger Configuration
# ========================
schema_view = get_schema_view(
    openapi.Info(
        title="CrashHub API",
        default_version='v1',
        description="CrashHub Complete API Documentation",
        contact=openapi.Contact(email="admin@crashhub.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# ========================
# URL Patterns
# ========================
urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Main APIs
    path('api/', include(router.urls)),

    # JWT Authentication
    path('api/auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger Docs
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]


