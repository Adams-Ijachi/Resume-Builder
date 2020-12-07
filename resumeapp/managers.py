from django.db import models


class GlobalModelQuerySet(models.QuerySet):
    def get_resume_data(self, pk):
        return self.filter(resume_id =pk)


class ResumeManger(models.Manager):
    def get_queryset(self):
        return GlobalModelQuerySet(self.model, using=self._db)

    def get_resume_information(self, pk):
        return self.get_queryset().get_resume_data(pk)
     
