from  django.urls import path
from .views import TaskListView, TaskDetail


urlpatterns = [
    path('tasks/', TaskListView.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()), 
]