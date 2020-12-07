from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse, HttpRequest
from resumeapp.models import Resume,PersonalInformation,Experience,Education,Skill
from resumeapp.forms import ResumeForm, ExperienceFormSet, PersonalInformationForm,EducationFormSet, SkillFormSet

# from StringIO import StringIO

# from django.template.loaders.base.loader 
from django.template.loader import render_to_string, get_template
from xhtml2pdf import pisa



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
    personal_info = get_object_or_404(PersonalInformation, resume_id=resume.id)
    workEXP= Experience.user_experiences.get_resume_information(resume.id)
    edu = Education.user_experiences.get_resume_information(resume.id)
    skills = Skill.user_experiences.get_resume_information(resume.id)
    resumes_template_path = resume.template.templates

    

    context['resume'] = resume
    context['temp_path'] = str(resumes_template_path)
    context['personal_info'] = personal_info
    context['workEXP'] = workEXP
    context['skills'] = skills
    context['edu'] = edu
  
    # resume_template =  render_to_string(f'{resumes_template_path}',context,request=request)
    
    return render(request, 'temp/basetemp.html', context)


def resume_download_pdf(request, pk , *args, **kwargs):
    context ={}

    resume = get_object_or_404(Resume, pk=pk)
    personal_info = get_object_or_404(PersonalInformation, resume_id=resume.id)
    print(personal_info.cover_image.url )
    workEXP= Experience.user_experiences.get_resume_information(resume.id)
    edu = Education.user_experiences.get_resume_information(resume.id)
    skills = Skill.user_experiences.get_resume_information(resume.id)
    resumes_template_path = resume.template.templates
    context['resume'] = resume
    context['temp_path'] = str(resumes_template_path)
    context['personal_info'] = personal_info
    context['workEXP'] = workEXP
    context['skills'] = skills
    context['edu'] = edu

    template_path = f'{resume.template.templates}'
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="resume.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
            html, dest=response
        )
    if pisa_status.err:
            return HttpResponse('bad')
    return response


    return HttpResponse(template_path) 


def resume_edit_view(request, pk , *args, **kwargs):
    template = get_object_or_404(Template, pk=pk)
    resume = ResumeForm(request.POST or None)
    personalInformation = PersonalInformationForm(request.POST or None, request.FILES or None)
    experienceForm = ExperienceFormSet(request.POST or None,queryset=Experience.objects.none(),prefix='Experience', )
    educationForm = EducationFormSet(request.POST or None,queryset=Education.objects.none(), prefix='Education')
    skillForm = SkillFormSet(request.POST or None,queryset=Skill.objects.none(),prefix='Skill')
    return render(request, 'pages/edit.html')
