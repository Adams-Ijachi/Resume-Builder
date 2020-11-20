from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from resumeapp.api import views



urlpatterns =[
    path('templates/', views.template_list, name='template_list')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)