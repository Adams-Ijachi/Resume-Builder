# Generated by Django 3.1.3 on 2020-11-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0008_auto_20201125_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='employer',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Employer'),
        ),
    ]