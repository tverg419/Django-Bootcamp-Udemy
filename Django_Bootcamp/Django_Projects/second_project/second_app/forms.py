from django import forms
from .models import UserInfo

class UserForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = '__all__'
