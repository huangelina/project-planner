from django.urls import path
from .views import create_task, list_of_tasks


urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", list_of_tasks, name="show_my_tasks"),
]
