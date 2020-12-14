from django.forms import ModelForm, Textarea,modelformset_factory, TextInput, CheckboxInput,ChoiceField, CharField,Select, FileInput, EmailInput, ImageField, ClearableFileInput
from .models import *

class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields  = ['summary']
        widgets = {
            'summary': Textarea(attrs={'cols': 80, 'rows': 6}),
        }
 

class PersonalInformationForm(ModelForm):
    class Meta:
        model = PersonalInformation
        exclude = ['resume','timestamp']
        widgets = {
            'firstname':TextInput(attrs={'class':'formset-field','class':'form-control','placeholder':'e.g. Adams'}),
            'lastname':TextInput(attrs={'class':'formset-field','class':'form-control','placeholder':'e.g. Ijachi'}),
            'cover_image':ClearableFileInput(),
            'address':TextInput(attrs={'class':'form-control','placeholder':'e.g. Dadin Kowa Jos'}),
            'country':Select(attrs={'class':'form-control'}),
            'state':TextInput(attrs={'class':'form-control','placeholder':'e.g. Plateau State '}),
            'email_address':EmailInput(attrs={'class':'form-control','placeholder':'e.g. adamsijachi9@gmail.com'}),
            'phone_number':TextInput(attrs={'class':'form-control','placeholder':'e.g. +2348143596560'}),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
      
        exclude = ['resume','timestamp']

        widgets = {
            'employer': TextInput(attrs={'class':'formset-field form-control','placeholder':'e.g. IBM '}),
            'job_title': TextInput(attrs={'class':'formset-field form-control','placeholder':'e.g. Engineer'}),
            'start_year': Select(attrs={'class':'form-control'}),
            'start_month': Select(attrs={'class':'form-control'}),
            'end_year': Select(attrs={'class':'form-control'}),
            'end_month': Select(attrs={'class':'form-control'}),
            'presently_work_here': CheckboxInput(attrs={'class':'presently_work_here '})
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ['resume','timestamp']
        widgets ={
            'school_name': TextInput(attrs={'class':'formset-field form-control','placeholder':'e.g. University of jos '}),
            'state':TextInput(attrs={'class':'formset-field form-control','placeholder':'e.g. Plateau State '}),
            'country':Select(attrs={'class':'form-control',}),
            'degree':TextInput(attrs={'class':'formset-field form-control','placeholder':'e.g. BSA '}),
            'field_of_study':TextInput(attrs={'class':'formset-field form-control','placeholder':'e.g. Computer Science '}),
            'graduation_month':Select(attrs={'class':'form-control'}),
            'graduation_year': Select(attrs={'class':'form-control'}),
            'presently_school_here': CheckboxInput(attrs={'class':'presently_school_here'}),
        
            
        }

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields  = ['name','level']
        widgets = {
            'name': TextInput(attrs={'class':'formset-field form-control','placeholder':'e.g. Python '}),
            'level':Select(attrs={'class':'form-control'}),

        }


SkillFormSet = modelformset_factory(Skill, form=SkillForm,can_delete=True)
EducationFormSet = modelformset_factory(Education, form=EducationForm,can_delete=True)
ExperienceFormSet = modelformset_factory(Experience, form=ExperienceForm,can_delete=True)


