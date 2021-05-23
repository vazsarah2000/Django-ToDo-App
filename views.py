from django.shortcuts import render , redirect
from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()
    form = taskform()

    if request.method == "POST":
        form = taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'tasks':tasks,'form':form}
    return render(request, 'task/list.html',context)

def update(request,pk):
    items = Task.objects.get(id=pk)
    form = taskform(instance=items)

    if request.method == "POST":
        form = taskform(request.POST , instance=items)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'form': form}
    return render(request, 'task/update.html', context)

def delete(request,pk):
    items = Task.objects.get(id=pk)

    if request.method == "POST":
        items.delete()
        return redirect("/")
    
    context = {'item':items}
    return render(request, 'task/delete.html',context)

