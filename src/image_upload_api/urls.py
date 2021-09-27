# coding=utf-8
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from image_upload_api.views import ArticleView

urlpatterns = [
    path('', ArticleView.as_view()),
    ]
