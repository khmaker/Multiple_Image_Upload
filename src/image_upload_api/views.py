# coding=utf-8
from django.views.generic import CreateView, DetailView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet

from image_upload_api.models import Article
from image_upload_api.serializers import ArticleSerializer


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    parser_classes = (MultiPartParser, FormParser)

