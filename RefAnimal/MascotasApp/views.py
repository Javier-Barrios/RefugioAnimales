
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from MascotasApp.models import mascota
from MascotasApp.forms import mascotaForm
from xhtml2pdf import pisa
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse




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


from django.template.loader import get_template
from xhtml2pdf import pisa



class mascotapdfView(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('mascota/list_pdf.html')
            context = {'mascota': mascota.objects.get(pk=self.kwargs['pk'])
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('MascotaApp:mascota_list'))



