# coding=utf-8
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from image_upload_api.models import Article
from image_upload_api.serializers import ArticleSerializer


class ArticleView(CreateAPIView):
    serializer_class = ArticleSerializer

    def get(self, request):
        instance, _ = Article.objects.get_or_create()
        context = {'request': request}
        serializer = ArticleSerializer(instance, context=context)
        return Response(serializer.data)
