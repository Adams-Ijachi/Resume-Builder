from django.contrib import admin
from .models import PersonalInformation,usersResume,Experience,Skill,About,Education, SkillTest
# Register your models here.



class usersResumeAdmin(admin.ModelAdmin):
    search_fields = ['user__username']
    list_display = ['__str__', 'user']
    
    class Meta:
        model = usersResume

admin.site.register(usersResume,usersResumeAdmin)
admin.site.register(PersonalInformation)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(About)
admin.site.register(Education)
admin.site.register(SkillTest)

