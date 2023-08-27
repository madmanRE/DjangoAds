from django import forms

from .models import AdvUser

class ProfileEditForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Электронная почта')
    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name', 'send_messages')