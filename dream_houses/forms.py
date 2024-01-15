from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'price','image', 'property_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'Property'}),
            'price': forms.NumberInput(attrs={'class': 'Property'}),
            'property_type':forms.TextInput(attrs={'class':Property}),
        }
        enctype = "multipart/form-data"  # Make sure this line is present

