from django import forms

from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    """Form definition for Test."""

    class Meta:
        """Meta definition for Testform."""
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',            
            )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
        
    def clean_cantidad(self):
        cantidad = self.cleaned_data["cantidad"]
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        
        return cantidad
        
