from django.urls import path, include

urlpatterns = [
    path('post/', include(('simpleblog.post.urls', 'post'))),
    path('auth/',   include(('simpleblog.authentication.urls', 'auth'))),
]
