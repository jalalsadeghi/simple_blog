from django.urls import path

from simpleblog.post.apis import ArticleApi

urlpatterns = [
    path("articles/", ArticleApi.as_view(), name="articles"),
]