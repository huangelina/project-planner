from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "projects/form_task.html", context)


@login_required
def list_of_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "list_of_tasks": tasks,
    }
    return render(request, "tasks/show_tasks.html", context)
