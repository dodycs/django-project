from django.urls import path
from . import views

app_name = 'project_manager'

urlpatterns = [
    # project
    path('', views.index, name='index'),
    path('create', views.create_project, name='create_project'),
    path('<int:project_id>/delete', views.delete_project, name='delete_project'),
    path('<int:project_id>/edit', views.edit_project, name='edit_project'),
    # task
    path('<int:project_id>/tasks', views.tasks, name='tasks'),
    path('<int:project_id>/task/create', views.create_task, name='create_task'),
    path('<int:project_id>/task/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('<int:project_id>/task/<int:task_id>/edit', views.edit_task, name='edit_task')
]
