from django import forms
from .models import Signup


class Signup_forms(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'

    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'aria - describedby': "basic-addon1",
                                   'placeholder': "Full Name"
                               }
                           ))
    email = forms.EmailField(max_length=50,
                             widget=forms.EmailInput(
                                 attrs={
                                     'class': 'form-control',
                                     'aria - describedby': "basic-addon1",
                                     'placeholder': "Email"
                                 }
                             ))
    password = forms.CharField(max_length=50,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                       'aria - describedby': "basic-addon1",
                                       'placeholder': "Password"
                                   }
                               ))
    mobile = forms.CharField(max_length=50,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'aria - describedby': "basic-addon1",
                                     'placeholder': "Mobile number"
                                 }))
