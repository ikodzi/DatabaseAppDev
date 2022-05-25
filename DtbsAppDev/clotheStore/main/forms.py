from .models import callBack
from django.forms import ModelForm, TextInput

class callBackForm(ModelForm):
    class Meta:
        model = callBack
        fields=[
            'name_call','number','email_call','message'
        ]

        widgets={
            "name_call":TextInput(attrs={
                'class':'form-control',
                'placeholder' : "Name"
            }),
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Phone number"
            }),
            "email_call": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Email"
            }),
            "message": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Message",
                'style':'height:250px'
            }),
        }