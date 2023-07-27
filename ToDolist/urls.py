from django.urls import path

from .views import TasksListView, TasksDetailView, UsersListView, UsersDetailView

urlpatterns = [
    path('tasks/', TasksListView.as_view(), name='tasks-list'),
    path('tasks/<int:pk>/', TasksDetailView.as_view(), name='tasks-detail'),
    path('users/', UsersListView.as_view(), name='users-list'),
    path('users/<int:pk>/', UsersDetailView.as_view(), name='users-detail')
]
