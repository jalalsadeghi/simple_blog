from simpleblog.contact.models import Contact
from config.env import env

from django.core.mail import send_mail

from django.db import transaction
from django.db.models import QuerySet
from django.utils import timezone




@transaction.atomic
def contact_create(*, email:str, name:str, content:str) -> QuerySet[Contact]:

    contact = Contact.objects.create(
        email = email,
        name = name,
        content = content,
    )
    send_mail(
        subject=name,
        message='name: '+name+'\n'+content+'\n'+'Reply-to: '+email,
        from_email=env('GMAIL_EMAIL_HOST_USER', default='noreply@simpleblog.com'),
        recipient_list=[env('EMAIL_SEND_TO_CONTACT', default='jalal.a.sadeghi@gmail.com')]
    )

    return contact