from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList

def index(request):
	#to get what to do
	to_do =  ToDoList.objects.all()
	context = {
		'to_do': to_do
	}
	return render(request, 'index.html',context)

def details(request, id):
	todo = ToDoList.objects.get(id=id)
	context = {
		'todo': todo
	}
	return render(request, 'details.html',context)

def add(request):
	if(request.method == 'POST'):
		title = request.POST['title']
		text = request.POST['text']
		task = ToDoList(title=title, text=text)
		task.save()

		return redirect('/core')
	else:
		return render(request, 'add.html')
