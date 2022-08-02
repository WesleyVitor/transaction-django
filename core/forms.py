from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from core.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, help_text='Fill Your Full Name.', label='Full_name')
    cpf =forms.CharField(max_length=11, help_text='Fill Your CPF.', label='CPF')
    email = forms.EmailField(max_length=200, required=True, help_text='Fill Your E-mail')
    password1 = forms.CharField(max_length=200, required=True, help_text='Fill Your Password.', label='Senha')
    password2 = forms.CharField(max_length=200, required=True, help_text='Fill Your Password Again.', label='Confirmar Senha')
    class Meta:
        model = CustomUser
        fields = ('email','full_name','cpf','password1','password2',)


class CustomUserChangeForm(UserChangeForm):

    full_name = forms.CharField(max_length=255, help_text='Fill Your Full Name.', label='Full_name')
    cpf =forms.CharField(max_length=11, help_text='Fill Your CPF.', label='CPF')
    email = forms.EmailField(max_length=200, required=True, help_text='Fill Your E-mail')
    password1 = forms.CharField(max_length=200, required=True, help_text='Fill Your Password.', label='Senha')
    password2 = forms.CharField(max_length=200, required=True, help_text='Fill Your Password Again.', label='Confirmar Senha')
    class Meta:
        model = CustomUser
        fields = ('email','full_name','cpf','password1','password2',)
    