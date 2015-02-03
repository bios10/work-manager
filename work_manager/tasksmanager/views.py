from django.shortcuts import render

from .models import Project


def index(request):
    action = 'Display project with client name = "Me"'
    projects_to_me = Project.objects.filter(client_name="Me")
    all_projects = Project.objects.all()
    return render(request, 'en/public/index.html', locals())

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'en/public/project_detail.html', {'project': project})

def connection(request):
    return render(request, 'en/public/connection.html')