from django.shortcuts import render, redirect , get_object_or_404, reverse
from django.http import HttpResponse, HttpRequest
from resumeapp.models import Resume,PersonalInformation,Experience,Education,Skill, Template
from django.db import transaction, IntegrityError
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
    if not request.user.is_authenticated:
        return redirect('/account/login/')
    context = {}
    resume = get_object_or_404(Resume, pk=pk)
    template = get_object_or_404(Template, pk=resume.template_id)
    personal_info = get_object_or_404(PersonalInformation, resume=resume.id)

    resume_data = {
        'summary':resume.summary
    }
    
    personalInformation_data = {
            'firstname':personal_info.firstname,
            'lastname':personal_info.lastname,
            'cover_image':personal_info.cover_image,
            'address':personal_info.address,
            'country':personal_info.country,
            'state':personal_info.state,
            'email_address':personal_info.email_address,
            'phone_number':personal_info.phone_number,
    }


    resumefORM = ResumeForm(request.POST or None, initial =resume_data, instance=resume)
    personalInformation = PersonalInformationForm(request.POST or None, request.FILES or None, initial=personalInformation_data, instance=personal_info)
    experienceForm = ExperienceFormSet(request.POST or None,queryset=Experience.user_experiences.get_resume_information(resume.id),prefix='Experience' )
    educationForm = EducationFormSet(request.POST or None,queryset=Education.user_experiences.get_resume_information(resume.id), prefix='Education')
    skillForm = SkillFormSet(request.POST or None,queryset=Skill.user_experiences.get_resume_information(resume.id),prefix='Skill',)


    if request.method == 'POST':
        if personalInformation.is_valid() and  educationForm.is_valid() and skillForm.is_valid() and experienceForm.is_valid() and  resumefORM.is_valid():
            try:
                with transaction.atomic():
                 

            
                    resumefORM.save()
                    personalInformation.save()
                    expInstances = experienceForm.save()
                    for expOBJ in expInstances:
                        if not expOBJ.resume  and expOBJ.employer:
                            expOBJ.resume = resume
                            expOBJ.save()
                    
                    eduInstances = educationForm.save()
                    for eduOBJ in eduInstances:
                        if not eduOBJ.resume and eduOBJ.school_name:
                            eduOBJ.resume = resume
                            eduOBJ.save()


                    skillInstances = skillForm.save()
                    for skillOBJ in skillInstances:
                        if not skillOBJ.resume and  skillOBJ.name :
                            skillOBJ.resume = resume
                            skillOBJ.save()

                    return redirect(reverse('resume_render', kwargs={'pk': resume.id}))
            except IntegrityError:
                return HttpResponse('error')
                       
                         
   
    context['skillForm'] = skillForm
    context['resume'] = resumefORM
    context['educationForm'] = educationForm
    context['experienceForm'] = experienceForm
    context['personalInformation'] = personalInformation 
    return render (request, 'form/formbase.html', context)
 

def resume_delete_view(request, pk , *args, **kwargs):
    
    resume = get_object_or_404(Resume, pk=pk)
    resume.delete()
    return redirect(reverse('profile_detail_view'))