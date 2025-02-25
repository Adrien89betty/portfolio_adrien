from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Votre nom"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Votre email"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Votre message"}),
        }
