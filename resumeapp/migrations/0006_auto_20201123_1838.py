# Generated by Django 3.1.3 on 2020-11-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0005_auto_20201119_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State'),
        ),
    ]
