from django.shortcuts import render
from AdopcionApp.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from AdopcionApp.forms import *

from django.urls import reverse_lazy




def adopcion_list(request):
    data = { 
        
        'title': 'Lista de Adopciones',
        'adopciones' : adopcion.objects.all()

    }
    return render(request, 'adopcion/list.html', data)

class adopcionListView(ListView):
    model = adopcion
    template_name = 'adopcion/list.html'
    context_object_name = 'adopcion'


class adopcionCreateView(CreateView):
    model = adopcion
    form_class= adopcionForm
    template_name = 'adopcion/create.html'
    success_url = reverse_lazy('AdopcionApp:adopcion_list') 
    

class adopcionUpdateView(UpdateView):
    model = adopcion
    form_class= adopcionForm
    template_name = 'adopcion/create.html'
    success_url = reverse_lazy('AdopcionApp:adopcion_list') 


class adopcionDeleteView(DeleteView):
    model = adopcion
    template_name = 'adopcion/delete.html'
    success_url = reverse_lazy('AdopcionApp:adopcion_list')