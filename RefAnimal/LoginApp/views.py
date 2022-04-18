from re import template
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from matplotlib.style import context

from UsuariosApp.models import Usuario
from MascotasApp.models import mascota
# Create your views here.

class LoginFormView(LoginView):
    template_name = 'LoginApp/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context

def account(request):
    mascotas= mascota.objects.all()
    informacion=Usuario.objects.all()
    context={'informacion': informacion, 'mascota':mascotas}
       
    return render(request, 'LoginApp/account.html', context)



def home(request):

    return render(request, "LoginApp/home.html")


def index(request):

    return render(request, "LoginApp/index.html")

def masinfo(request):
    mascotas= mascota.objects.all()
    informacion=Usuario.objects.all()
    context={'informacion': informacion, 'mascota':mascotas}

    return render(request, "LoginApp/masinfo.html", context)



#def details(request, id, Type2_id):
#    mascotas= mascota.objects.all()
#    informacion=Usuario.objects.all()
#    masc= mascota.objects.get(id=id)
#    tipo = mascota.objects.get(Type2_id=Type2_id)
#    return redirect('/detalle')