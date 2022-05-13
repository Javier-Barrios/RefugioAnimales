from django.shortcuts import render, redirect

from UsuariosApp.forms import UsuariosForm
from UsuariosApp.models import Usuario
from django.contrib import messages
from UsuariosApp.models import Usuario
from UsuariosApp.models import  *
from UsuariosApp.forms import *
from django.conf import settings

import requests
from django.views.generic import  UpdateView, DeleteView, View
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from xhtml2pdf import pisa
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import get_template

# Create your views here.

def registroadmin(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        edad = request.POST['edad']
        photo = request.POST.get('photo')
        password = request.POST['password']
        #type = request.POST['type']
        form = UsuariosForm(request.POST, request.FILES)
        if form.is_valid():
                photo = form.cleaned_data.get("photo")
                recaptcha_response = request.POST.get('g-recaptcha-response')

                data = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response                   


                }

                r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data) 
                result = r.json()

                if Usuario.objects.filter(username=username).exists():
                    messages.info(request, 'El nombre de usuario "Username" ya existe')
                    return redirect('/registrar')
                elif Usuario.objects.filter(email=email).exists():
                    messages.info(request, 'El correo "Email" ya fue registrado anteriormente')
                    return redirect('/registrar')

                elif result['success']:
                    user = Usuario.objects.create_user(username = username, password = password, email=email, first_name=first_name, last_name=last_name, edad=edad, photo=photo)
                    user.save();
                    messages.info(request, 'El nuevo usuario ha sido registrado exitosamente')
                    username = request.POST.get('username')
                    password = request.POST.get('password')

                    user = authenticate(request=request,username=username, password=password)
                    login(request, user)
                    print("Usuario registrado")
                    return redirect('/credencial')

                else:
                    messages.error(request, 'Utilice el recaptcha')
                    return redirect('/registrar')


 #               if result['success']:
#                    user = Usuario.objects.create_user(username = username, password = password, email=email, first_name=first_name, last_name=last_name, edad=edad, photo=photo)
#                    user.save();
#                    messages.info(request, 'El nuevo usuario ha sido registrado exitosamente')
#                    username = request.POST.get('username')
#                    password = request.POST.get('password')

  #                  user = authenticate(request=request,username=username, password=password)
  #                  login(request, user)
 #                   print("Usuario registrado")
 #                   return redirect('/credencial')
#
#                else:
#                    messages.error(request, 'Utilice el recaptcha')
#                    return redirect('/registrar')

#        if Usuario.objects.filter(username=username).exists():
#            messages.info(request, 'El nombre de usuario "Username" ya existe')
#            return redirect('/account')
#        elif Usuario.objects.filter(email=email).exists():
#            messages.info(request, 'El correo "Email" ya fue registrado anteriormente')
#            return redirect('/account')
#        else
#            user = Usuario.objects.create_user(username = username, password = password, email=email, first_name=first_name, last_name=last_name, edad=edad, photo=photo)
#            user.save();
#            messages.info(request, 'El nuevo usuario ha sido registrado exitosamente')
#            print("Usuario registrado")
#            return redirect('/account')     
    else:
        context['form'] = UsuariosForm()
        return render(request, "usuarios/registrar.html", context)

def form_photo(request):
    context = {}
    context['form'] = UsuariosForm()
    return render(request, "usuarios/registrar.html", context)


def credencial(request):
    informacion=Usuario.objects.all()
    context ={'informacion': informacion}
    return render(request, "usuarios/credencial.html", context)

def listadouser(request):
    informacion=Usuario.objects.all()
    context ={'informacion': informacion}
    return render(request, "usuarios/usuariolist.html", context)

def comments(request):
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CommentForm()

    return render(request, 'RecaptchaForm.html', {'form': form})


def perfil(request):
    informacion = Usuario.objects.all()
    context = {'informacion': informacion}
    return render(request, 'usuarios/perfil.html', context)


class usuarioUpdateView(UpdateView):
    model = Usuario
    form_class= usuarioForm
    template_name = 'usuarios/actualizar.html'
    success_url = reverse_lazy('usuarioslist') 

class usuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/delete.html'
    success_url = reverse_lazy('usuarioslist')



class usuariopdfView(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('usuarios/list_pdf.html')
            context = {'usuarios': Usuario.objects.get(pk=self.kwargs['pk'])
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
        return HttpResponseRedirect(reverse_lazy('UsuariosApp:usuario_list'))