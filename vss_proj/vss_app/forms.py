from django import forms
import re
class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.EmailField()

    phone = forms.CharField(
        max_length=10,
        min_length=10,
        error_messages={
            "min_length": "Phone number must be exactly 10 digits.",
            "max_length": "Phone number must be exactly 10 digits.",
        }
    )

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        return phone

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get("password")
        cpwd = cleaned_data.get("confirm_password")
        if pwd != cpwd:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    
from .models import UserFeedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Tell us what you think...'
            })
        }
    