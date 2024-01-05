from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import ModelForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    tasks = Task.objects.all()
    return render(request, 'mytodo/home.html', {'tasks': tasks})

class Addtodo(CreateView):
    model = Task
    template_name = 'mytodo/form.html'
    fields = '__all__'
    
class Updatetodo(UpdateView):
    model = Task
    template_name = 'mytodo/update.html'
    fields = '__all__'
    
class Deletetodo(DeleteView):
    model = Task
    success_url = reverse_lazy('home')