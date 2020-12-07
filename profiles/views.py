from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse, HttpRequest
from resumeapp.models import Resume
# from StringIO import StringIO
import os 
from io import BytesIO
# from django.template.loaders.base.loader 
from django.template.loader import render_to_string
from django.core.files import File

# Create your views here.

def profile_resume_list_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        next = 'profiles'
        return redirect('/account/login/')
    user_resume = Resume.objects.filter(user=request.user).order_by("-timestamp")
    return render(request, 'pages/profiles.html', {'user_resume':user_resume})

def resume_render_view(request, pk , *args, **kwargs):
    context = {}
    resume = get_object_or_404(Resume, pk=pk)
    context['resume'] = resume

    resumes_template_path = resume.template.templates
    context['temp_path'] = str(resumes_template_path)

    resume_template =  render_to_string(f'{resumes_template_path}',context,request=request)
    
    return render(request, 'temp/basetemp.html', context)

