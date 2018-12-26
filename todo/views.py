from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.generic import CreateView
from django.views.decorators.http import require_POST


def index(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm
    context= {
        'todo_list': todo_list,
        'form': form
    }
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_post = Todo(text=form.cleaned_data['text'])
        new_post.save()
    return redirect('todo-index')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('todo-index')

def deleteComplete(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('todo-index')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('todo-index')
