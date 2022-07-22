from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, "appcore/index.html")


@login_required
def read_all(request):

    return render(request, "appcore/read_all.html", {
        "header": f"{request.user.username}'s tasks",
        "tasks": Task.objects.filter(tasked_to=request.user).order_by("-id")
    })


@login_required
def create(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            try:
                new_task = Task.objects.create(
                    name = form.cleaned_data["name"],
                    description = form.cleaned_data["description"],
                    created_on = timezone.now(),
                    due_on = timezone.now(),
                    is_completed = False,
                    tasked_to = request.user
                )
                new_task.save()
                messages.success(request, "Task created")
                return HttpResponseRedirect(reverse("read_all"))
            except Exception as e:
                messages.error(request, f"Error: Save failed ({e.__cause__})")
                return render(request, "appcore/create.html", {
                    "form": TaskForm(instance=form)
                })
        else:
            messages.error(request, "Error: Form not valid")
            return render(request, "appcore/create.html", {
                "form": TaskForm(instance=form)
            })
    else:
        return render(request, "appcore/create.html", {
            "form": TaskForm()
        })


@login_required
def read(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.user != task.tasked_to:
        messages.error(request, "Error: Not your task")
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        return render(request, "appcore/read_one.html", {
            "task": task.__dict__
        })


@login_required
def update(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.user != task.tasked_to:
        messages.error(request, "Error: Not your task")
        return redirect(request.META.get("HTTP_REFERER"))

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            try:
                task.name = form.cleaned_data["name"]
                task.description = form.cleaned_data["description"]
                # task.due_on = form.cleaned_data["due_on"],
                # task.is_completed = form.cleaned_data["is_completed"]
                task.save(
                    update_fields=[
                        "name",
                        "description",
                        # "due_on",
                        # "is completed"
                ])
                messages.success(request, "Task updated")
                return HttpResponseRedirect(reverse("read_all"))
            except Exception as e:
                messages.error(request, f"Error: Failed to save ({e.__cause__})")
                return render(request, "appcore/update.html", {
                    "form": TaskForm(instance=task),
                    "id": task_id
                })
        else:
            messages.error(request, "Error: Form not valid")
            return render(request, "appcore/update.html", {
                "form": TaskForm(instance=task),
                "id": task_id

            })
    else:
        return render(request, "appcore/update.html", {
                "form": TaskForm(instance=task),
                "task": task
            })


@login_required
def delete(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.user != task.tasked_to:
        messages.error(request, "Error: not your task")
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        try:
            task.delete()
            messages.success(request, "Task deleted")
        except:
            messages.error(request, "Error: failed to delete")
    return redirect(request.META.get("HTTP_REFERER"))
