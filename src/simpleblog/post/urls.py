from django.urls import path

from simpleblog.post.apis import ArticleApi, PostDetailApi

urlpatterns = [
    path("articles/", ArticleApi.as_view(), name="articles"),
    path("post_detail/<int:id>/<slug:slug>/", PostDetailApi.as_view(), name="post_detail"),
]