from msilib.schema import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from refugioapp.models import empleado
from refugioapp.forms import empleadoForm



def empleado_list(request):
    data = { 
        
        'title': 'Listado de Empleados',
        'empleados' : empleado.objects.all()

    }
    return render(request, 'empleado/list.html', data)


class empleadoListView(ListView):
    model = empleado
    template_name = 'empleado/list.html'
    

class empleadoCreateView(CreateView):
    model = empleado
    form_class= empleadoForm
    template_name = 'empleado/create.html'
    success_url = reverse_lazy('refugioapp:empleado_list') 
    

class empleadoUpdateView(UpdateView):
    model = empleado
    form_class= empleadoForm
    template_name = 'empleado/create.html'
    success_url = reverse_lazy('refugioapp:empleado_list') 


class empleadoDeleteView(DeleteView):
    model = empleado
    template_name = 'empleado/delete.html'
    success_url = reverse_lazy('refugioapp:empleado_list')








