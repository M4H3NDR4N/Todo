from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST # decorators restrict access to views based on request method.

from .models import Todo
from .forms import TodoForm

def index(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'todo_app/todo_list.html', context)

@require_POST # The view accepts only the POST Method
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete() #deletes a model from DB.

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete() # Deletes the whole model.

    return redirect('index')
