# Generated by Django 4.1.4 on 2022-12-11 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('project_desc', models.CharField(max_length=250)),
                ('project_link', models.CharField(max_length=250)),
            ],
        ),
    ]
