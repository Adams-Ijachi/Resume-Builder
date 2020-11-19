from django.shortcuts import render, redirect
# from .forms import TemplateForm
# from .models import Template, User

# Create your views here.


# def templateslist(request):
   
#     templates = Template.objects.all()
#     return render(request, 'home.html', {'templates':templates}) # file = request.FILES['D']


# def templatesUpload(request):
#     form = TemplateForm()
#     if request.method == 'POST':
#        form = TemplateForm(request.POST , request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('tempList')
#     return render(request, 'upload.html', {'form':form}) # file = request.FILES['D']

# def delete(request, pk):
#     if request.method =='POST':
#         temp = Template.objects.get(pk=pk)
#         temp.delete()
#         return redirect('tempList')


# def user(request):
#     user = User.objects.get(id=1)
#     print(user)
#     return 