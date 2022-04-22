from django.urls import path

from AdopcionApp.views import *


app_name= 'AdopcionApp'

urlpatterns = [
    path('adopcion/list/', adopcionListView.as_view(), name='adopcion_list'),
    path('adopcion/add/', adopcionCreateView.as_view(), name='adopcion_create'),
    path('adopcion/edit/<int:pk>/', adopcionUpdateView.as_view(), name='adopcion_update'),
    path('adopcion/delete/<int:pk>/', adopcionDeleteView.as_view(), name='adopcion_delete'),
  

]