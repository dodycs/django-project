from django.shortcuts import render, redirect
from django.contrib import messages

from . import models as m

# PROJECT
def index(request):
	if 'user_id' in request.session:
		context = {
			'projects': m.Project.objects.filter(user_id=request.session['user_id']).order_by('-updated_at')
		}
		return render(request, 'project_manager/project/index.html', context)
	return redirect('login_registration:login')

def create_project(request):
	if request.method == 'POST':
		try:
			project = m.Project()
			project.title = request.POST['title']
			project.user_id = request.session['user_id']
			project.save()
		except:
			messages.error(request, 'Title cannot be blank')
		return redirect('project_manager:index')

def delete_project(request, project_id):
	if request.method == 'GET':
		project = m.Project.objects.get(id=project_id)
		project.delete()
		return redirect('project_manager:index')

def edit_project(request, project_id):
	project = m.Project.objects.get(id=project_id)
	context = {'project_id': project.id}
	if request.method == 'POST':
		try:
			project.title = request.POST['title']
			project.save()
			return redirect('project_manager:index')
		except:
			messages.error(request, 'Title cannot be blank')

	context = {
		'project' : project
	}
	return render(request, 'project_manager/project/edit.html', context)

# TASK
def tasks(request, project_id):
	tasks = m.Task.objects.filter(project_id=project_id)
	context = {
		'project_id':project_id,
		'tasks': tasks
	}
	return render(request, 'project_manager/task/index.html', context)

def create_task(request, project_id):
	if request.method == 'POST':
		try:
			task = m.Task()
			task.project_id = project_id
			task.description = request.POST['description']
			task.save()
		except:
			messages.error(request, 'Description cannot be blank')

	context = {
		'project_id': project_id,
		'tasks': m.Task.objects.filter(project_id=project_id)
	}
	return render(request, 'project_manager/task/index.html', context)

def delete_task(request, project_id, task_id):
	if request.method == 'GET':
		try:
			task = m.Task.objects.get(id=task_id)
			task.delete()
		except:
			messages.error(request, 'Failed delete task')
	return redirect('project_manager:tasks', project_id=project_id)

def edit_task(request, project_id, task_id):
	task = m.Task.objects.get(id=task_id)
	if request.method == 'POST':
		try:
			task.description = request.POST['description']
			task.save()
			return redirect('project_manager:tasks', project_id=project_id)
		except:
			messages.error(request, 'Description cannot be blank')
	
	context = {
		'project_id': project_id,
		'task_id': task_id,
		'task': task
	}
	return render(request, 'project_manager/task/edit.html', context)
