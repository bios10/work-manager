# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=50)),
                ('description', models.CharField(verbose_name='Description', max_length=1000)),
                ('client_name', models.CharField(verbose_name='Client name', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=50)),
                ('description', models.CharField(verbose_name='Description', max_length=1000)),
                ('time_elapsed', models.IntegerField(verbose_name='Elapsed time', null=True, default=None, blank=True)),
                ('importance', models.IntegerField(verbose_name='Importance')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=50)),
                ('login', models.CharField(verbose_name='Login', max_length=25)),
                ('password', models.CharField(verbose_name='Password', max_length=100)),
                ('phone', models.CharField(verbose_name='Phone number', null=True, max_length=20, default=None, blank=True)),
                ('born_date', models.DateField(verbose_name='Born date', null=True, default=None, blank=True)),
                ('last_connection', models.DateTimeField(verbose_name='Date of last connection', null=True, default=None, blank=True)),
                ('email', models.EmailField(verbose_name='Email', max_length=75)),
                ('years_seniority', models.IntegerField(verbose_name='Seniority', default=0)),
                ('date_created', models.DateField(verbose_name='Date of Birthday', auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tasksmanager.UserProfile')),
                ('specialization', models.CharField(verbose_name='Specialization', max_length=50)),
            ],
            options={
            },
            bases=('tasksmanager.userprofile',),
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('userprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tasksmanager.UserProfile')),
                ('supervisor', models.ForeignKey(verbose_name='Supervisor', to='tasksmanager.Supervisor')),
            ],
            options={
            },
            bases=('tasksmanager.userprofile',),
        ),
        migrations.AddField(
            model_name='task',
            name='app_user',
            field=models.ForeignKey(verbose_name='Developer', to='tasksmanager.Developer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(verbose_name='Project', null=True, default=None, blank=True, to='tasksmanager.Project'),
            preserve_default=True,
        ),
    ]
