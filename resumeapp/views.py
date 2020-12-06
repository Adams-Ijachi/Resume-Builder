from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.db import transaction, IntegrityError
from .forms import ResumeForm, ExperienceFormSet, PersonalInformationForm,EducationFormSet, SkillFormSet
from .models import Template, Experience, Education, Skill,Resume

# Create your views here.


def home(request):
    templates = Template.objects.all()
    return render(request, 'pages/index.html', {'templates':templates}) # file = request.FILES['D']


def resumeUpload(request,pk):
    context = {}
    template = get_object_or_404(Template, pk=pk)
    resume = ResumeForm(request.POST,initial={'template':template})
    personalInformation = PersonalInformationForm()
    experienceForm = ExperienceFormSet(queryset=Experience.objects.none(),prefix='Experience', )
    educationForm = EducationFormSet(queryset=Education.objects.none(), prefix='Education')
    context['experienceForm'] = experienceForm
    context['resume'] = resume
    context['personalInformation'] = personalInformation
    context['educationForm'] = educationForm
    
    return render(request, 'upload.html', context) # file = request.FILES['D']

def formRender(request, pk, *args, **kwargs):
    context = {}
    if not request.user.is_authenticated:
        return redirect('/account/login/')
    template = get_object_or_404(Template, pk=pk)
    resume = ResumeForm(request.POST or None)
    personalInformation = PersonalInformationForm(request.POST or None, request.FILES or None)
    experienceForm = ExperienceFormSet(request.POST or None,queryset=Experience.objects.none(),prefix='Experience', )
    educationForm = EducationFormSet(request.POST or None,queryset=Education.objects.none(), prefix='Education')
    skillForm = SkillFormSet(request.POST or None,queryset=Skill.objects.none(),prefix='Skill')
    
    if request.method == 'POST':
        resume = ResumeForm(request.POST or None,instance=request.user)
        personalInformation = PersonalInformationForm(request.POST,request.FILES)
        if personalInformation.is_valid() and  educationForm.is_valid() and skillForm.is_valid() and experienceForm.is_valid() and  resume.is_valid():

            try:
                with transaction.atomic():
           
                    summary= resume.cleaned_data['summary']
                    resumes = Resume(user=request.user, template=template,summary=summary)
                    resumes.save()
                
                    obj = personalInformation.save(commit=False)
                    obj.resume = resumes
                    obj.save() 

                    for experience in experienceForm:
                        expOBJ = experience.save(commit=False)
                        expOBJ.resume = resumes
                        if expOBJ.presently_work_here:
                            expOBJ.end_year = None
                            expOBJ.end_month = None
                        expOBJ.save()
                    
                    for education in educationForm:
                        eduOBJ = education.save(commit=False)
                        eduOBJ.resume = resumes
                        if eduOBJ.presently_school_here:
                            eduOBJ.graduation_month = None
                            eduOBJ.graduation_year = None
                        eduOBJ.save()
                    
                    for skill in skillForm:
                        skillOBJ = skill.save(commit=False)
                        skillOBJ.resume = resumes
                        skillOBJ.save()
            except IntegrityError:
                print('error')
               # return      
        return HttpResponse(request.POST)
    context['skillForm'] = skillForm
    context['resume'] = resume
    context['educationForm'] = educationForm
    context['experienceForm'] = experienceForm
    context['personalInformation'] = personalInformation 
    return render (request, 'form/formbase.html', context)

# def formSaveandPDf(request):
#     if request.method == 'POST':





# def user(request):
#     user = User.objects.get(id=1)
#     print(user)
#     return 

#     if request.method == 'POST':s
#        form = TemplateForm(request.POST , request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('tempList')