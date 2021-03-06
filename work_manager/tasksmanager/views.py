from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Project, Supervisor, Developer, error_name


class form_inscription(forms.Form):
    name = forms.CharField(label="Name", max_length=30, error_messages=error_name)
    login = forms.CharField(label="Login", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_bis = forms.CharField(label="Password", widget=forms.PasswordInput)
    supervisor = forms.ModelChoiceField(label="Supervisor", queryset=Supervisor.objects.all())

    def clean(self):
        cleaned_data = super(form_inscription, self).clean()
        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')
        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
        return self.cleaned_data


class form_supervisor(forms.ModelForm):
    class Meta:
        model = Supervisor
        exclude = ('date_created', 'last_connexion', )


def index(request):
    action = 'Display project with client name = "Me"'
    projects_to_me = Project.objects.filter(client_name="Me")
    all_projects = Project.objects.all()
    return render(request, 'en/public/index.html', locals())


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'en/public/project_detail.html', {'project': project})


def create_developer(request):
    if request.POST:
        form = form_inscription(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            supervisor = form.cleaned_data['supervisor']
            new_developer = Developer(name=name, login=login, password=password,
                                      email="", supervisor=supervisor)
            new_developer.save()
            return HttpResponse("Developer added")
        else:
            return render(request, 'en/public/create_developer.html', {'form': form})
    else:
        form = form_inscription()
        return render(request, 'en/public/create_developer.html', {'form': form})


def create_supervisor(request):
    if len(request.POST) > 0:
        form = form_supervisor(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('public_index'))
        else:
            return render(request, 'en/public/create_supervisor.html', {'form': form})
    else:
        form = form_supervisor()
        return render(request, 'en/public/create_supervisor.html', {'form': form})


def connection(request):
    return render(request, 'en/public/connection.html')