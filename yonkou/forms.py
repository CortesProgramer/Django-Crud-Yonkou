from django import forms


class LuffyForm(forms.Form):
    OPCIONES_HAKI = [
        ("armadura", "Haki de armadura"),
        ("observacion", "Haki de observacion"),
        ("rey", "Haki del rey")
    ]
    nombre = forms.CharField(label="nombre", max_length=25)
    haki = forms.ChoiceField(label="Haki a entrenar", choices=OPCIONES_HAKI, widget=forms.Select)
    edad = forms.IntegerField(label="edad")
    dia = forms.CharField(label="dia", max_length=15)
    hora = forms.CharField(label="hora", max_length=10)
    

class ShanksForm(forms.Form):
    OPCIONES_HAKI = [
        ("armadura", "Haki de armadura"),
        ("observacion", "Haki de observacion"),
        ("rey", "Haki del rey")
    ]
    nombre = forms.CharField(max_length=25)
    haki = forms.ChoiceField(label="Haki a entrenar", choices=OPCIONES_HAKI, widget=forms.Select)
    edad = forms.IntegerField()
    dia = forms.CharField(max_length=25)
    hora = forms.CharField(max_length=25)
    
    
class TeachForm(forms.Form):
    OPCIONES_HAKI = [
        ("armadura", "Haki de armadura"),
        ("observacion", "Haki de observacion"),
        ("rey", "Haki del rey")
    ]
    nombre = forms.CharField(max_length=25)
    haki = forms.ChoiceField(label="haki a entrenar", choices=OPCIONES_HAKI, widget=forms.Select)
    edad = forms.IntegerField()
    dia = forms.CharField(max_length=25)
    hora = forms.CharField(max_length=25)
    
    
class BuggyForm(forms.Form):
    OPCIONES_HAKI = [
        ("armadura", "Haki de armadura"),
        ("observacion", "Haki de observacion"),
        ("rey", "Haki del rey")
    ]
    nombre = forms.CharField(max_length=25)
    haki = forms.ChoiceField(label="haki a entrenar", choices=OPCIONES_HAKI, widget=forms.Select)
    edad = forms.IntegerField()
    dia = forms.CharField(max_length=25)
    hora = forms.CharField(max_length=25)