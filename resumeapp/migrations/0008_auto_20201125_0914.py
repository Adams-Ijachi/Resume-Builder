# Generated by Django 3.1.3 on 2020-11-25 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0007_auto_20201124_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='resume/template_image/', verbose_name='Cover_Image'),
        ),
        migrations.AddField(
            model_name='template',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='user/cover_image/', verbose_name='Cover_Image'),
        ),
    ]
