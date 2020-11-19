import datetime
from django.db import models
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from django.conf import settings

YEAR_CHOICES = [(y,y) for y in range(1968, datetime.date.today().year+1)]
MONTH_CHOICE = [(m,m) for m in range(1,13)]
User = settings.AUTH_USER_MODEL

# Create your models here.
class Template(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
  #   cover_image = models.ImageField(verbose_name='Cover_Image',upload_to='resume/cover_image/', null=True, blank=True)
    templates = models.FileField(upload_to='resume/templates/')


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, blank= True)
    skills = models.ManyToManyField("Skill",verbose_name="Skill")
    summary= models.TextField(max_length=100, verbose_name='Professional Summary')
    timestamp = models.DateTimeField(auto_now_add=True)

   


class PersonalInformation(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, verbose_name='First Name')
    lastname = models.CharField(max_length=100, verbose_name='Last Name')
    cover_image = models.ImageField(verbose_name='Cover_Image',upload_to='resume/cover_image/', null=True, blank=True)
    address = models.CharField(max_length=200, verbose_name='Address',null=True, blank=True)
    country = CountryField(blank_label='(select country)')
    email_address = models.EmailField(max_length=254, verbose_name='Email Address')
    phone_number = models.CharField(max_length=15, verbose_name='Phone Number',null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.resume.user.username


class Experience(models.Model):


    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    employer = models.CharField(max_length=100, verbose_name='Employer')
    job_title = models.CharField(max_length=100, verbose_name='Job Title',null=True, blank=True)
    start_year = models.IntegerField(choices=YEAR_CHOICES,default=datetime.datetime.now().year,null=True, blank=True)
    start_month = models.IntegerField(choices=MONTH_CHOICE,default=datetime.datetime.now().month,null=True, blank=True)
    end_year = models.IntegerField(choices=YEAR_CHOICES,default=datetime.datetime.now().year,null=True, blank=True)
    end_month = models.IntegerField(choices=MONTH_CHOICE,default=datetime.datetime.now().month,null=True, blank=True)
    presently_work_here = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.resume.user.username

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100, verbose_name='School Name',null=True, blank=True)
    country = CountryField(blank_label='(select country)')
    state = models.CharField(max_length=100, verbose_name='State',null=True, blank=True)
    degree = models.CharField(max_length=100, verbose_name='Degree',null=True, blank=True)
    field_of_study = models.CharField(max_length=100, verbose_name='Field Of Study',null=True, blank=True)
    graduation_month = models.IntegerField(choices=YEAR_CHOICES,default=datetime.datetime.now().year,null=True, blank=True)
    graduation_year = models.IntegerField(choices=MONTH_CHOICE,default=datetime.datetime.now().month,null=True, blank=True)
    presently_school_here = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.resume.user.username

class Skill(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class About(models.Model):
#    user = models.ForeignKey(, on_delete=models.CASCADE)
#    summary= models.TextField(max_length=100, verbose_name='Professional Summary')
#    timestamp = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#         return self.user.username


# class usersResume(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     personalInformation = models.ForeignKey(PersonalInformation, on_delete=models.SET_NULL, null=True)
#     experience = models.ForeignKey(Experience, on_delete=models.SET_NULL, null=True)
#     education = models.ForeignKey(Education, on_delete=models.SET_NULL, null=True)
#     skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)
#     skilltests = models.ManyToManyField(User, related_name='user_skill',blank=True, through=SkillTest, verbose_name='Skill Test')
#     about = models.ForeignKey(About, on_delete=models.SET_NULL, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username



  
# class SkillTest(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     cv = models.ForeignKey("usersResume", on_delete=models.CASCADE)
#     skill = models.CharField(max_length=20, verbose_name='SkillTest')
#     level = models.IntegerField(null=True, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
        return self.user.username

    







# class Template(models.Model):
#     title = models.CharField(max_length=100)
#     cover_image = models.ImageField(verbose_name='Cover_Image',upload_to='resume/cover_image/', null=True, blank=True)
#     templates = models.FileField(upload_to='resume/templates/')
    

#     def __str__(self):
#         return self.title

#     def delete(self, *args, **kwargs):
#         self.templates.delete()
#         self.cover_image.delete()
#         super().delete(*args, **kwargs)

# class User(models.Model):
#     name = models.CharField(max_length=20)
#     def __str__(self):
#         return self.name
    


# class Skills(models.Model):
#     skills = models.CharField(max_length=20, verbose_name='Skills')
#     level = models.IntegerField(null=True, blank=True)
#     user = models.ManyToManyField(User, )

#     def __str__(self):
#         return self.skills



