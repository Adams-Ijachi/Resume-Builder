from django.shortcuts import render, redirect,get_object_or_404
from .forms import ResumeForm, ExperienceFormSet, PersonalInformationForm,EducationFormSet
from .models import Template, Experience, Education

# Create your views here.


def home(request):
    context = {}
    personalInformation = PersonalInformationForm()
    experienceForm = ExperienceFormSet(queryset=Experience.objects.none(),prefix='Experience', )
    context['experienceForm'] = experienceForm
    return render(request, 'form/form.html', context) # file = request.FILES['D']


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

def form(request):
    context = {}
    personalInformation = PersonalInformationForm()
    experienceForm = ExperienceFormSet(queryset=Experience.objects.none(),prefix='Experience', )
    context['personalInformation'] = personalInformation
    context['experienceForm'] = experienceForm
    return render (request, 'form/formbase.html', context)


# def user(request):
#     user = User.objects.get(id=1)
#     print(user)
#     return 

#     if request.method == 'POST':s
#        form = TemplateForm(request.POST , request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('tempList')