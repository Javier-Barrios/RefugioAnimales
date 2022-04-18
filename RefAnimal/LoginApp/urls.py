from django.urls import path

from LoginApp import views

from MascotasApp.views import mascotaListView

urlpatterns = [
    path('',views.home, name='Home'),
 



    path('index',views.index, name='Index'),
    path('masinfo',views.masinfo, name='masinfo'),
    path('mascota/list/', mascotaListView.as_view(), name='mascota_list'),
    


]