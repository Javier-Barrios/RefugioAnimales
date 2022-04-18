from django.forms import ModelForm
from refugioapp.models import empleado

class empleadoForm(ModelForm):

    class Meta:
        model = empleado
        fields = '__all__'
        
