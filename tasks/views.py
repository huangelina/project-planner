from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm


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
