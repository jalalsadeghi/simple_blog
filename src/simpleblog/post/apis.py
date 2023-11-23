from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from drf_spectacular.utils import extend_schema
from django.urls import reverse

from simpleblog.api.pagination import  LimitOffsetPagination, get_paginated_response_context
from simpleblog.post.models import  Article
from simpleblog.post.selectors import article_list


class ArticleApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 5

    class OutPutPostSerializer(serializers.ModelSerializer):
        author = serializers.SerializerMethodField("get_author")
        # url = serializers.SerializerMethodField("get_url")

        class Meta:
            model = Article
            fields = ("title", "author")    #"url",

        def get_author(self, post):
            return post.author.username

        # def get_url(self, post):
        #     request = self.context.get("request")
        #     path = reverse("api:post_detail", args=(post.slug,))
        #     return request.build_absolute_uri(path)

    @extend_schema(
        responses=OutPutPostSerializer,
    )
    def get(self, request):

        try:
            query = article_list()
        except Exception as ex:
            return Response(
                {"detail": "Filter Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return get_paginated_response_context(
            pagination_class=self.Pagination,
            serializer_class=self.OutPutPostSerializer,
            queryset=query,
            request=request,
            view=self,
        )