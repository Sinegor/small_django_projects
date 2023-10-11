from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    [print(task) for task in tasks]
# при указании адреса шаблона мы исходим из того, что интерпритатор уже сразу перейдёт в папку templates:
    return render(request, 'main_app/index.html',{'title':'Main page',
                                                  'tasks':tasks})

def about(request):
    return render(request, 'main_app/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error= "Форма было неверной!"
    
    form = TaskForm()
    context = {
        'form':form,
        'error':error
    }
    return render (request, 'main_app/create.html', context)
