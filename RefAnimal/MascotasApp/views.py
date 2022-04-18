from msilib.schema import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from MascotasApp.models import mascota
from MascotasApp.forms import mascotaForm




def mascota_list(request):
    data = { 
        
        'title': 'Listado de Mascotass',
        'mascotas' : mascota.objects.all()

    }
    return render(request, 'mascota/list.html', data)


class mascotaListView(ListView):
    model = mascota
    template_name = 'mascota/list.html'
    

class mascotaCreateView(CreateView):
    model = mascota
    form_class= mascotaForm
    template_name = 'mascota/create.html'
    success_url = reverse_lazy('MascotasApp:mascota_list') 
    

class mascotaUpdateView(UpdateView):
    model = mascota
    form_class= mascotaForm
    template_name = 'mascota/create.html'
    success_url = reverse_lazy('MascotasApp:mascota_list') 


class mascotaDeleteView(DeleteView):
    model = mascota
    template_name = 'mascota/delete.html'
    success_url = reverse_lazy('MascotasApp:mascota_list')






