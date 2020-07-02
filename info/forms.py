from django import forms
from info.models import Contactus , Trainingmodel
class Contactform(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'
class Trainingform(forms.ModelForm):
    class Meta:
        model = Trainingmodel
        fields = '__all__'
