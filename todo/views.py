from django.shortcuts import render, redirect
from todo.models import Todo
from todo.forms import TodoForm


def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo/todo_list.html', context)


def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo
    }
    return render(request, 'todo/todo_detail.html', context)


def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo:todo_list')

    context = {
        'form': form
    }
    return render(request, 'todo/todo_create.html', context)


def todo_update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo:todo_list')

    context = {
        'form': form
    }
    return render(request, 'todo/todo_update.html', context)


def todo_delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo:todo_list')