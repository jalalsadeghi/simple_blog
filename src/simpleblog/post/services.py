from simpleblog.post.models import Article

from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import QuerySet
from django.utils.text import slugify


@transaction.atomic
def post_create(*, user:User, title:str, content:str) -> QuerySet[Article]:

    post = Article.objects.create(
        author  = user,
        title   = title,
        content = content,
        slug    = slugify(title)
    )
    return post