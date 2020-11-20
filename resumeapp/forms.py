from django.forms import ModelForm, Textarea,modelformset_factory, TextInput
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
        }
        
       
    
ExperienceFormSet = modelformset_factory(Experience, form=ExperienceForm)

