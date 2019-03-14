from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('faq', views.faq, name='faq'),
    path('rsvp', views.rsvp, name='rsvp'),
    path('submit_rsvp', views.submit_rsvp, name='submit_rsvp'),
    path('talks', views.presentations, name='presentations'),
    path('submit', views.submit, name='submit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
