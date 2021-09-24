# coding=utf-8
from django.db.models import (
    CASCADE, FileField, ForeignKey, Model, TextField,
)


class Article(Model):
    text = TextField()


class Image(Model):
    image = FileField()
    article = ForeignKey(
        'Article',
        on_delete=CASCADE,
        related_name='images'
    )
