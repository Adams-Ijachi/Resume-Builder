from django.forms import ModelForm, Textarea,modelformset_factory, TextInput, CheckboxInput,ChoiceField, CharField,Select, FileInput, EmailInput
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
            'cover_image':FileInput(),
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
            'employer': TextInput(attrs={'class':'formset-field form-control'}),
            'job_title': TextInput(attrs={'class':'formset-field form-control'}),
            'start_year': Select(attrs={'class':'form-control'}),
            'start_month': Select(attrs={'class':'form-control'}),
            'end_year': Select(attrs={'class':'form-control'}),
            'end_month': Select(attrs={'class':'form-control'}),
            'presently_work_here': CheckboxInput(attrs={'class':'presently_work_here ','onClick':'endYearAndMonthDisplay($(this))'})
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ['resume','timestamp']
        widgets ={
            'school_name': TextInput(attrs={'class':'formset-field'}),
            'state':TextInput(attrs={'class':'formset-field'}),
            'degree': TextInput(attrs={'class':'formset-field'}),
            'field_of_study': TextInput(attrs={'class':'formset-field'}),
            'presently_school_here': CheckboxInput(attrs={'class':'presently_school_here','onClick':'log($(this))'}),
        
            
        }
   
    
ExperienceFormSet = modelformset_factory(Experience, form=ExperienceForm)

EducationFormSet = modelformset_factory(Education, form=EducationForm)
