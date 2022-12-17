# Generated by Django 4.1.4 on 2022-12-15 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
        ('all_projects_list', '0003_alter_projectlist_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectlist',
            name='belongs_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_profile.userprofile'),
        ),
    ]