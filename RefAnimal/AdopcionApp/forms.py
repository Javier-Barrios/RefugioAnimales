from asyncio import selector_events
from select import select
from tkinter.tix import Select
from django import forms
from django.forms import ModelForm, SelectMultiple, TextInput, Textarea
from django import forms
from matplotlib import widgets


from AdopcionApp.models import adopcion


class adopcionForm(ModelForm):
    class Meta:
        model = adopcion
        fields = '__all__'
        labels = {
            'nombre':'nombre'
        }
        widgets = {
            'nombre': TextInput(
                attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'autocomplete': 'off'
                }
            ),
            'apellido': TextInput(
                attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido',
                    'autocomplete': 'off'
                }
            ),
            'edad': TextInput(
                attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ingrese su edad',
                    'autocomplete': 'off'
                }
            ),
            'email': TextInput(
                attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ingrese su email',
                    'autocomplete': 'off'
                }
            ),
            'numero': TextInput(
                attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ingrese su numero',
                    'autocomplete': 'off'
                }
            ),
            'domicilio': TextInput(
                attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ingrese su domicilio',
                    'autocomplete': 'off'
                }
            ),
            'mascota': TextInput(
                attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre de su peludito',
                    'autocomplete': 'off'
            
                }
            ),
            'razon_para_adoptar': Textarea(
                attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus razones para adoptar',
                    'autocomplete': 'off'
            
                }
            ),
            
        } 
            
          