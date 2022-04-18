from django.urls import path

from refugioapp.views.empleado.view import *

app_name= 'refugioapp'

urlpatterns = [
    path('empleado/list/', empleadoListView.as_view(), name='empleado_list'),
    path('empleado/add/', empleadoCreateView.as_view(), name='empleado_create'),
    path('empleado/edit/<int:pk>/', empleadoUpdateView.as_view(), name='empleado_update'),
    path('empleado/delete/<int:pk>/', empleadoDeleteView.as_view(), name='empleado_delete'),

]