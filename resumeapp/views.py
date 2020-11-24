from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .forms import ResumeForm, ExperienceFormSet, PersonalInformationForm,EducationFormSet, SkillFormSet
from .models import Template, Experience, Education, Skill

# Create your views here.


def home(request):
    return render(request, 'pages/index.html') # file = request.FILES['D']

def login(request):
    return render (request, 'accounts/login.html')
def resumeUpload(request,pk):
    context = {}
    template = get_object_or_404(Template, pk=pk)
    resume = ResumeForm(initial={'template':template})

    personalInformation = PersonalInformationForm()
    experienceForm = ExperienceFormSet(queryset=Experience.objects.none(),prefix='Experience', )
    educationForm = EducationFormSet(queryset=Education.objects.none(), prefix='Education')
    context['experienceForm'] = experienceForm
    context['resume'] = resume
    context['personalInformation'] = personalInformation
    context['educationForm'] = educationForm
    
    return render(request, 'upload.html', context) # file = request.FILES['D']

def formRender(request):
    context = {}
    personalInformation = PersonalInformationForm()
    experienceForm = ExperienceFormSet(queryset=Experience.objects.none(),prefix='Experience', )
    educationForm = EducationFormSet(queryset=Education.objects.none(), prefix='Education')
    skillForm = SkillFormSet(queryset=Skill.objects.none(),prefix='Skill')
    context['skillForm'] = skillForm
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