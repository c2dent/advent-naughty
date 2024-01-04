from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main import views

urlpatterns = [
                  path('djrichtextfield/', include('djrichtextfield.urls')),
                  path('advent/<int:user_id>/', views.advent, name='advent'),
                  path('send-message/', views.send_message, name='send_message'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('', admin.site.urls),
]
