# Generated by Django 4.1.4 on 2022-12-31 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0002_remove_technologieslist_belongs_to'),
        ('user_profile', '0005_rename_github_url_userprofile_github_handle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tech_worked_with',
            field=models.ManyToManyField(blank=True, null=True, to='technologies.technologieslist'),
        ),
    ]