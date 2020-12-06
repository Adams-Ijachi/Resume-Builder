from django.urls import path 
from profiles import views

urlpatterns = [ 
 path('resumes', views.profile_resume_list_view, name = 'profile_detail_view'),
 path('resume/render/<int:pk>',views.resume_render_view, name='resume_render')
]