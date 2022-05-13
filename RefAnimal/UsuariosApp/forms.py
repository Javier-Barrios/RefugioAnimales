from django import forms
from django.forms import ModelForm
from UsuariosApp.models import Usuario
from django.contrib.auth.forms import UserChangeForm
from django.forms import TextInput

class UsuariosForm(forms.Form):
    photo = forms.ImageField()

class EditarPerfilForm(ModelForm):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'edad',
            'photo',
        )

        widgets = {
            'username': TextInput(
                attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ingrese su usuario',
                    'autocomplete': 'off'
                }
            ),
            'first_name': TextInput(
                attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'autocomplete': 'off'
                }
            ),
            'last_name': TextInput(
                attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido',
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
            'edad': TextInput(
                attrs = { 
                    'class': 'form-control',
                    'placeholder': 'Ingrese su edad',
                    'autocomplete': 'off'
                }
            ),             
            
        }



class usuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'edad',
            'photo',
        )


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        required=True,
        max_length=1000
    )