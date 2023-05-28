from django import forms
from .models import Information


class Medkit_Information(forms.ModelForm):
    class Meta():
        model = Information
        fields = ['medicine_name', 'expiry_date', 'quantity',
                  'marked_price', 'description', 'discount', 'company', 'dealer']

        widgets = {
            'medicine_name': forms.TextInput(attrs={'class': 'form-control', 'name': 'medicine_name'}),
            'expiry_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'name': 'expiry_date'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'name': 'quantity', 'id':'quantity'}),
            'marked_price': forms.TextInput(attrs={'class': 'form-control', 'name': 'marked_price'}),
            'discount': forms.TextInput(attrs={'class': 'form-control', 'name': 'discount'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'name':'desc'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'name': 'company'}),
            'dealer': forms.TextInput(attrs={'class': 'form-control', 'name': 'dealer'}),
        }


class Sale_Information(forms.ModelForm):
    class Meta():
        model = Information
        fields = ['quantity']

        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'name': 'quantity'}),
        }

class Add_Information(forms.ModelForm):
    class Meta():
        model = Information
        fields = ['quantity']

        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'name': 'quantity'}),
        }
    

