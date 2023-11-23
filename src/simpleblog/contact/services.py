from simpleblog.contact.models import Contact

from django.db import transaction
from django.db.models import QuerySet


@transaction.atomic
def contact_create(*, email:str, name:str, content:str) -> QuerySet[Contact]:

    contact = Contact.objects.create(
        email = email,
        name = name,
        content = content,
    )
    return contact