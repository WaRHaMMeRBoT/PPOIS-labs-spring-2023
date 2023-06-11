
from .models import Medicine
from django import forms


class Form(forms.ModelForm):
    name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=30)
    date_of_birth = forms.CharField(max_length=30)
    date_of_visit = forms.CharField(max_length=30)
    name_of_doctor = forms.CharField(max_length=30)
    conclusion = forms.CharField(max_length=30)

    class Meta:
        model = Medicine
        fields = ("name", "address", "date_of_birth", "date_of_visit", "name_of_doctor", "conclusion")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'address': forms.TextInput(attrs={'class': 'form-input'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-input'}),
            'date_of_visit': forms.TextInput(attrs={'class': 'form-input'}),
            'name_of_doctor': forms.TextInput(attrs={'class': 'form-input'}),
            'conclusion': forms.TextInput(attrs={'class': 'form-input'}),
        }
