from django.urls import path

from MascotasApp.views import *

app_name= 'MascotasApp'

urlpatterns = [
    path('mascota/list/', mascotaListView.as_view(), name='mascota_list'),
    path('mascota/add/', mascotaCreateView.as_view(), name='mascota_create'),
    path('mascota/edit/<int:pk>/', mascotaUpdateView.as_view(), name='mascota_update'),
    path('mascota/delete/<int:pk>/', mascotaDeleteView.as_view(), name='mascota_delete'),
    path('mascota/list_pdf/<int:pk>/', mascotapdfView.as_view(), name='mascota_pdf'),

]