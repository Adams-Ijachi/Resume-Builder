from django.urls import path 
from profiles import views

urlpatterns = [ 
path('resumes', views.profile_resume_list_view, name = 'profile_detail_view'),
path('resume/render/<int:pk>',views.resume_render_view, name='resume_render'),
path('resume/download/<int:pk>', views.resume_download_pdf, name='Download_PDF'),
path('resume/edit/<int:pk>', views.resume_edit_view, name='Edit_resume'),

]