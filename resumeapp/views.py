from django.shortcuts import render, redirect,get_object_or_404
from .forms import ResumeForm, ExperienceFormSet, PersonalInformationForm
from .models import Template, Experience

# Create your views here.


def home(request):
    return render(request, 'home.html') # file = request.FILES['D']


def resumeUpload(request,pk):
    context = {}
    template = get_object_or_404(Template, pk=pk)
    resume = ResumeForm(initial={'template':template})
    personalInformation = PersonalInformationForm()
    experienceForm = ExperienceFormSet(queryset=Experience.objects.none(),prefix='Experience')
    context['experienceForm'] = experienceForm
    context['resume'] = resume
    context['personalInformation'] = personalInformation
    return render(request, 'upload.html', context) # file = request.FILES['D']

# def delete(request, pk):
#     if request.method =='POST':
#         temp = Template.objects.get(pk=pk)
#         temp.delete()
#         return redirect('tempList')


# def user(request):
#     user = User.objects.get(id=1)
#     print(user)
#     return 

#     if request.method == 'POST':s
#        form = TemplateForm(request.POST , request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('tempList')