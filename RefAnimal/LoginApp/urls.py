from django.urls import path

from LoginApp import views

from MascotasApp.views import mascotaListView
from AdopcionApp.views import *
from LoginApp.views import masinfo

urlpatterns = [
    
 



    path('',views.index, name='Index'),
    path('masinfo',views.masinfo, name='masinfo'),
    path('mascota/list/', mascotaListView.as_view(), name='mascota_list'),
    path('adopcion/list/', adopcionListView.as_view(), name='adopcion_list'),
    path('<slug:nombre>/animal/<int:id>', masinfo),


]