from django.forms import ModelForm
from MascotasApp.models import mascota

class mascotaForm(ModelForm):

    class Meta:
        model = mascota
        fields = '__all__'
        
