"""RefAnimal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from LoginApp.views import *
from MascotasApp.views import *
from refugioapp.views.empleado.view import *
from django.conf.urls.static import static
from django.conf import settings
from UsuariosApp.views import *
from ReconocimientoApp.views import *
from AdopcionApp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='LoginApp/login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='Index.html'), name='logout'),
    path('', include('LoginApp.urls')),    
    path('', include('MascotasApp.urls')),
    path('', include('refugioapp.urls')),
    path('', include('AdopcionApp.urls')),
    #path('home/', include('EmpleadosApp.urls')),
    path("account/", account, name="account"),
    path('adopcion/add/', adopcionCreateView.as_view(), name='adopcion_create'),
    path('registrar/', registroadmin, name='registrar'),
    path('perfil/', perfil, name='perfil'),

    path('credencial/', credencial, name='credencial'),

    path('usuarioslist/', listadouser, name='usuarioslist'),

    path('usuario/edit/<int:pk>/', usuarioUpdateView.as_view(), name='usuario_update'),
    path('usuario/delete/<int:pk>/', usuarioDeleteView.as_view(), name='usuario_delete'),

    path('perfil/crear/', biometrico, name='biometrico'),
    
    path('crear/', biometrico2, name='biometrico2'),
    
    path('entrenador/', trainer, name='entrenador'),
    path('detect/', detect, name="detectar"),
    path("detect/cuenta/<int:id>", deteccion, name="deteccion"),
    #path('test/', TestView.as_view(), name='test'),


    path('usuarios/list_pdf/<int:pk>/',usuariopdfView.as_view(), name='usuario_pdf'),


        # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),



    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

