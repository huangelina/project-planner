from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required


@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "project_list": projects,
    }
    return render(request, "projects/list_projects.html", context)
