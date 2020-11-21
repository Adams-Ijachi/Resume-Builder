from django.forms import ModelForm, Textarea,modelformset_factory, TextInput, CheckboxInput,ChoiceField
from .models import Resume, Experience, PersonalInformation

class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields  = ['skills','summary']
        widgets = {
            'summary': Textarea(attrs={'cols': 80, 'rows': 6}),
        }


class PersonalInformationForm(ModelForm):
    class Meta:
        model = PersonalInformation
      
        exclude = ['resume','timestamp']

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
      
        exclude = ['resume','timestamp']

        widgets = {
            'employer': TextInput(attrs={'class':'formset-field'}),
            'job_title': TextInput(attrs={'class':'formset-field'}),

            # 'end_year': TextInput(attrs={'class':'formset-field'}),
            # 'end_month': TextInput(attrs={'class':'formset-field'}),

            'presently_work_here': CheckboxInput(attrs={'class':'presently_work_here','onClick':'log($(this))'})
        }
        
       
    
ExperienceFormSet = modelformset_factory(Experience, form=ExperienceForm, extra=3)

