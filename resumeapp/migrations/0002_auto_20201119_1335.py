# Generated by Django 3.1.3 on 2020-11-19 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume_skills', to='resumeapp.resume'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.ManyToManyField(related_name='skills', to='resumeapp.Skill', verbose_name='Skill'),
        ),
    ]
