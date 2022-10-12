from django.urls import path
from .views import TaskListView, TaskDetail, AssignTask, TaskDone


urlpatterns = [
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("tasks/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("tasks/<int:pk>/assign", AssignTask.as_view(), name="task_assigned"),
    path("tasks/<int:pk>/done", TaskDone.as_view(), name="task_done"),
]
