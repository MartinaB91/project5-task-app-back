from  django.urls import path
from .views import TaskListView, TaskDetail, AssignTask


urlpatterns = [
    path('tasks/', TaskListView.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()), 
    path('tasks/<int:pk>/assign', AssignTask.as_view()), 
]