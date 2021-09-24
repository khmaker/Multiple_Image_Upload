# coding=utf-8
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from image_upload_api.views import ArticleViewSet

v1_router = DefaultRouter()
v1_router.register(
    'articles',
    ArticleViewSet,
    basename='articles'
    )
urlpatterns = [
    path('', include(v1_router.urls)),
    ]
