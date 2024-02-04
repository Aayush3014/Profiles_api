from django.urls import path, include
from .views import UserProfileViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('userprofile',UserProfileViewSet)

urlpatterns = [
    path('',include(router.urls))
]