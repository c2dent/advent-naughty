from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from main import views

urlpatterns = [
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('advent/<int:user_id>/', views.advent, name='advent'),
    path('send-message/', views.send_message, name='send_message'),
] + [re_path(r"^static/(?P<path>.*)$", serve), re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

urlpatterns += [
    path('', admin.site.urls),
]