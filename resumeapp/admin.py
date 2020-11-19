from django.contrib import admin
from .models import PersonalInformation,Experience,Skill,Education,Resume, Template
# Register your models here.

class EducationAdmin(admin.TabularInline):
    model= Education

class SkillAdmin(admin.TabularInline):
    model= Skill

class PersonalInformationAdmin(admin.TabularInline):
    model= PersonalInformation

class ExperienceAdmin(admin.TabularInline):
    model= Experience

class ResumeAdmin(admin.ModelAdmin):

    search_fields = ['user__username']
    list_display = ['__str__', 'user',]
    inlines = [SkillAdmin,ExperienceAdmin,PersonalInformationAdmin,EducationAdmin]
    class Meta:
         model = Resume

admin.site.register(Resume,ResumeAdmin)
admin.site.register(Template)


 