from django.shortcuts import render
from AdopcionApp.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from AdopcionApp.forms import *
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

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
    success_url = reverse_lazy('AdopcionApp:adopcion_exitosa') 
    

class adopcionExitosaView(CreateView):
    model = adopcion
    form_class= adopcionForm
    template_name = 'adopcion/solicitud_exitosa.html'
    success_url = reverse_lazy('AdopcionApp:adopcion_exitosa') 
    

class adopcionUpdateView(UpdateView):
    model = adopcion
    form_class= adopcionForm
    template_name = 'adopcion/create.html'
    success_url = reverse_lazy('AdopcionApp:adopcion_list') 


class adopcionDeleteView(DeleteView):
    model = adopcion
    template_name = 'adopcion/delete.html'
    success_url = reverse_lazy('AdopcionApp:adopcion_list')


class adopcionpdfView(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('adopcion/list_pdf.html')
            context = {'adopcion': adopcion.objects.get(pk=self.kwargs['pk'])
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
        return HttpResponseRedirect(reverse_lazy('Adopcionapp:adopcion_list'))
