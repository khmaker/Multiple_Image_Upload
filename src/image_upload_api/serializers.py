# coding=utf-8
from rest_framework.serializers import ModelSerializer

from image_upload_api.models import Article, Image


class ImageSerializer(ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class ArticleSerializer(ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        article, _ = Article.objects.update_or_create(id=1)
        article.text = validated_data.pop('text')
        article.save(update_fields=['text'])
        for image_data in images_data.values():
            Image.objects.create(article=article, image=image_data)
        return article
