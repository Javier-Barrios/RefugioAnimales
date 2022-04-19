from django.urls import path

from LoginApp import views

from MascotasApp.views import mascotaListView
from LoginApp.views import masinfo

urlpatterns = [
    
 



    path('',views.index, name='Index'),
    path('masinfo',views.masinfo, name='masinfo'),
    path('mascota/list/', mascotaListView.as_view(), name='mascota_list'),
    path('<slug:nombre>/animal/<int:id>', masinfo),


]