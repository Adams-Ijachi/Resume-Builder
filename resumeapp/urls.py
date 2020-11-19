from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from resumeapp import views

urlpatterns = [
   
    # # path('', views.home, name='home'),
    # # path('upload', views.upload, name='upload'),
    # path('',views.templateslist, name='tempList'),
    # path('upload',views.templatesUpload, name='templatesUpload' ),
    # path('temp/delete/<int:pk>', views.delete, name='delete_temp')

]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)