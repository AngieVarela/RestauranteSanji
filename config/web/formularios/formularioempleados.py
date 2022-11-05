from django import forms

class FormularioEmpleados (forms.Form):

    CARGO=(
        (1,'Cheff'),
        (2,'Administrador'),
        (3,'Mesero'),
        (3,'Ayudante'),
    )

    nombre=forms.CharField(
        required=True,
        max_length=5,
        label='Nombre Empleado: ',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    apellidos=forms.CharField(
        required=True,
        max_length=5,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    fotografia=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    cargo=forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-control mb-3'}),
        choices=CARGO
    )
    salario=forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class': 'form-control mb-3'})
    )
    contacto=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )