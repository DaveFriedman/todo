from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("read", views.read_all, name="read_all"),
    path("read/<int:task_id>", views.read, name="read"),
    path("update/<int:task_id>", views.update, name="update_task"),
    path("delete/<int:task_id>", views.delete, name="delete"),
]
